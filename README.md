# 🎨 Virtual_Painter

A real-time **Virtual Painter** built using **Python, OpenCV, and MediaPipe**. Draw in the air using your index finger, switch colors with simple hand gestures, and erase drawings—all without touching the screen.

---

## ✨ Features

- 🖐️ Real-time hand tracking using MediaPipe
- ✍️ Air drawing using finger gestures
- 🎨 Multiple brush colors
  - 🔴 Red
  - 🟢 Green
  - 🔵 Blue
  - 🩷 Pink
  - 🟡 Yellow
  - 🟣 Purple
  - ⚪ White
- 🧽 Eraser tool
- 📌 Smooth brush movement
- 🖼️ Interactive toolbar for color selection
- ⚡ Fast and responsive performance

---

## 🛠️ Built With

- Python
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Project Structure

```text
Virtual_Painter/
│
├── Colors/
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   ├── 6.jpg
│   └── 7.jpg
│
├── HandTrackingModule.py
├── VirtualPainter.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/arjunvallala/Virtual_Painter.git
```

### 2. Navigate to the project folder

```bash
cd Virtual_Painter
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python VirtualPainter.py
```

---

## 🖐️ Hand Gestures

### ✍️ Drawing Mode
- Raise **only the Index Finger**.
- Move your finger to draw on the canvas.

### 🎨 Selection Mode
- Raise **Index Finger + Middle Finger**.
- Move your fingers over the toolbar to:
  - Select a brush color
  - Select the eraser

---

## 🎨 Available Tools

| Tool | Function |
|------|----------|
| 🔴 Red | Draw with a red brush |
| 🟢 Green | Draw with a green brush |
| 🔵 Blue | Draw with a blue brush |
| 🩷 Pink | Draw with a pink brush |
| 🟡 Yellow | Draw with a yellow brush |
| 🟣 Purple | Draw with a purple brush |
| ⚪ White | Draw with a white brush |
| 🧽 Eraser | Remove drawings |

---

## 📦 Requirements

```
opencv-python
mediapipe
numpy
```

Install manually if needed:

```bash
pip install opencv-python mediapipe numpy
```

---

## ⚡ How It Works

1. Captures live video from the webcam.
2. Detects hand landmarks using MediaPipe.
3. Identifies finger gestures.
4. Switches between Drawing Mode and Selection Mode.
5. Draws on a virtual canvas.
6. Combines the canvas with the webcam feed using OpenCV bitwise operations.

---

## 🚀 Future Improvements

- Adjustable brush thickness
- Save drawing as an image
- Undo/Redo support
- Shape drawing tools
- Custom color picker
- Keyboard shortcuts
- Brush effects

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates further improvements.
