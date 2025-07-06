from fpdf import FPDF

# Strict ASCII cleaner
def ascii_clean(text):
    return text.encode("ascii", "ignore").decode("ascii")

class JawlineWorkoutPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, ascii_clean("Jawline Workout Chart (Printable)"), ln=True, align="C")
        self.ln(5)

    def add_exercise(self, title, steps, reps):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 120)
        self.cell(0, 10, f"- {ascii_clean(title)}", ln=True)
        self.set_font("Arial", "", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, f"  Steps: {ascii_clean(steps)}\n  Reps: {ascii_clean(reps)}")
        self.ln(2)

# Create PDF
pdf = JawlineWorkoutPDF()
pdf.add_page()

# Exercises list
exercises = [
    {
        "title": "Chin Lifts",
        "steps": "Tilt your head back, look at the ceiling, push your lower jaw forward to feel a stretch under your chin. Hold for 10 seconds.",
        "reps": "10 reps"
    },
    {
        "title": "Jaw Clenching",
        "steps": "Clench your jaw tightly, hold for 10 seconds, then relax. Do not grind teeth.",
        "reps": "10 reps"
    },
    {
        "title": "Tongue Press",
        "steps": "Press your tongue against the roof of your mouth. Hum to activate neck muscles.",
        "reps": "15 reps"
    },
    {
        "title": "Fish Face",
        "steps": "Suck your cheeks in and try to smile. Hold the pose for 15 seconds.",
        "reps": "5 sets"
    },
    {
        "title": "Chewing Gum",
        "steps": "Chew sugar-free gum continuously to activate jaw muscles.",
        "reps": "15-20 minutes"
    }
]

# Add all exercises
for ex in exercises:
    pdf.add_exercise(ex["title"], ex["steps"], ex["reps"])

# Output
pdf.output("Jawline_Workout_Chart.pdf")
print("✅ PDF created: Jawline_Workout_Chart.pdf")
