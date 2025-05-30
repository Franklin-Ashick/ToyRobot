# 🤖 Toy Robot Simulator

This is a simple but fun simulation of a toy robot that moves around on a 5x5 grid.

You can place the robot at any position and tell it to move forward, rotate left, or rotate right. The robot follows the commands in the exact order you give them — and it always avoids falling off the table!

The simulator also shows you:
- The robot’s starting position
- Its movement direction
- The final position and direction
- A full history of commands run

It's all interactive and visual — built using Python and Streamlit.

---

## 🛠️ Setup Instructions

Here's how to get everything running on your local machine:

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate the environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```


### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> If you don’t have a requirements.txt, just install manually:
```bash
pip install streamlit matplotlib
```

---

## 🚀 Run the Simulator

After installing everything, run the app with:
```bash
streamlit run toyrobot.py
```

This will launch the simulator in your browser. You can:
- Choose where to place the robot
- Add commands like MOVE, LEFT, RIGHT
- Run everything with a single click
- Watch the robot move on a grid in real time

---

## 🧪 Example

### Input:

PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE


### Final Output:

3,3,NORTH


---

## 💡 Notes

- The robot will never move off the grid — it ignores commands that would cause that.
- You don’t need to type commands — just click buttons to build your sequence.
- The simulator uses matplotlib to show grid movement with arrows and coordinates.

---

## 📬 Questions?

If you're reviewing this or using it in a test — hope it gives a clear idea of my coding style, UI focus, and logic implementation.

