import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Toy Robot Simulator Logic
# -------------------------------
class ToyRobotSimulator:
    def _init_(self):
        self.reset()

    def reset(self):
        self.x = None
        self.y = None
        self.facing = None
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.placed = False
        self.command_history = []
        self.initial_position = None

    def place(self, x, y, facing):
        if 0 <= x <= 4 and 0 <= y <= 4 and facing in self.directions:
            self.x = x
            self.y = y
            self.facing = facing
            self.placed = True
            if not self.initial_position:
                self.initial_position = (x, y, facing)

    def move(self):
        if not self.placed:
            return
        if self.facing == "NORTH" and self.y < 4:
            self.y += 1
        elif self.facing == "EAST" and self.x < 4:
            self.x += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1

    def left(self):
        if not self.placed:
            return
        self.facing = self.directions[(self.directions.index(self.facing) - 1) % 4]

    def right(self):
        if not self.placed:
            return
        self.facing = self.directions[(self.directions.index(self.facing) + 1) % 4]

    def report(self):
        if not self.placed:
            return None
        return f"{self.x},{self.y},{self.facing}"

    def execute_command(self, command):
        self.command_history.append(command)
        command = command.strip().upper()
        if command == "MOVE":
            self.move()
        elif command == "LEFT":
            self.left()
        elif command == "RIGHT":
            self.right()

    def execute_multiple_commands(self, commands):
        for line in commands.strip().split("\n"):
            self.execute_command(line.strip())

    def draw_robot(self, ax, x, y, facing, label):
        ax.plot(x, y, 'ro', markersize=12)
        arrow = {
            "NORTH": (0, 0.4),
            "SOUTH": (0, -0.4),
            "EAST": (0.4, 0),
            "WEST": (-0.4, 0)
        }
        dx, dy = arrow.get(facing, (0, 0))
        ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
        ax.text(x + 0.2, y + 0.2, label, fontsize=9, color='green')

# -------------------------------
# Streamlit Interface
# -------------------------------
st.set_page_config(page_title="Toy Robot Simulator", layout="wide")
st.markdown("<h1 style='text-align:center;'>🤖 Toy Robot Simulator</h1>", unsafe_allow_html=True)

simulator = ToyRobotSimulator()

# Session state for command list
if "command_list" not in st.session_state:
    st.session_state.command_list = []

# Step 1: Placement UI
with st.expander("🔧 Step 1: Place the Robot", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.selectbox("X Coordinate", range(5), key="x")
    with col2:
        y = st.selectbox("Y Coordinate", range(5), key="y")
    with col3:
        facing = st.selectbox("Facing Direction", ["NORTH", "EAST", "SOUTH", "WEST"], key="facing")

# Step 2: Command buttons
with st.expander("🎮 Step 2: Add Commands", expanded=True):
    st.markdown("Click buttons to build your command sequence:")
    cmd1, cmd2, cmd3, cmd4 = st.columns(4)
    with cmd1:
        if st.button("MOVE"):
            st.session_state.command_list.append("MOVE")
    with cmd2:
        if st.button("LEFT"):
            st.session_state.command_list.append("LEFT")
    with cmd3:
        if st.button("RIGHT"):
            st.session_state.command_list.append("RIGHT")
    with cmd4:
        if st.button("🗑️ Clear All"):
            st.session_state.command_list.clear()

    if st.session_state.command_list:
        st.success("📜 Your Command Sequence")
        st.code("\n".join(st.session_state.command_list))
    else:
        st.info("No commands added yet.")

# Step 3: Run and visualize
with st.expander("🚀 Step 3: Run Simulation", expanded=True):
    if st.button("🏁 Place and Execute"):
        simulator.reset()
        simulator.place(x, y, facing)
        simulator.command_history.append(f"PLACE {x},{y},{facing}")
        simulator.execute_multiple_commands("\n".join(st.session_state.command_list))

        # Grid Visualization
        st.markdown("### 🧭 Grid Visualization")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        for ax in [ax1, ax2]:
            ax.set_xlim(-0.5, 4.5)
            ax.set_ylim(-0.5, 4.5)
            ax.set_xticks(range(5))
            ax.set_yticks(range(5))
            ax.set_xticklabels([f"{i}" for i in range(5)], fontsize=10)
            ax.set_yticklabels([f"{i}" for i in range(5)], fontsize=10)
            ax.set_facecolor("#f0f0f0")
            ax.grid(True, linestyle="--", color="gray", alpha=0.7)
            ax.set_aspect('equal')
            ax.set_xlabel("X", fontsize=12, labelpad=10)
            ax.set_ylabel("Y", fontsize=12, labelpad=10)

        if simulator.initial_position:
            x0, y0, f0 = simulator.initial_position
            simulator.draw_robot(ax1, x0, y0, f0, "Placed")

        if simulator.placed:
            simulator.draw_robot(ax2, simulator.x, simulator.y, simulator.facing, "Now")

        ax1.set_title("Initial Placement", fontsize=14, fontweight='bold')
        ax2.set_title("Final Position", fontsize=14, fontweight='bold')
        st.pyplot(fig)

        # Command log
        st.markdown("### 📚 Full Command History")
        for cmd in simulator.command_history:
            st.write(f"✅ {cmd}")

        # Final report
        st.markdown("### 📢 Final Output")
        report = simulator.report()
        if report:
            st.success(f"Robot Output: {report}")
        else:
            st.error("❌ Robot was not placed.")