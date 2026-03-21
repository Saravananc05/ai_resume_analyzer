import tkinter as tk
from tkinter import ttk
# ---------- SKILLS DATABASE ----------
job_roles = {
    "Python Developer": ["python", "django", "flask", "api", "sql"],
    "Data Scientist": ["python", "machine learning", "pandas", "numpy", "data analysis"],
    "Web Developer": ["html", "css", "javascript", "react", "node"]
}
# ---------- ANALYZER ----------
def analyze_resume(resume_text, role):
    resume_text = resume_text.lower()
    required_skills = job_roles.get(role, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100) if required_skills else 0
    return score, matched, missing
# ---------- FUNCTION ----------
def run_analysis():
    resume = text_box.get("1.0", tk.END)
    role = role_var.get()

    score, matched, missing = analyze_resume(resume, role)
    # Update Progress Bar
    progress['value'] = score
    score_label.config(text=f"{score}%")
    # Clear output
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    # Insert Results
    result_box.insert(tk.END, "✅ Matched Skills:\n", "green")
    result_box.insert(tk.END, ", ".join(matched) if matched else "None")
    result_box.insert(tk.END, "\n\n")

    result_box.insert(tk.END, "❌ Missing Skills:\n", "red")
    result_box.insert(tk.END, ", ".join(missing) if missing else "None")

    result_box.config(state="disabled")
# ---------- GUI ----------
root = tk.Tk()
root.title("AI Resume Analyzer Pro")
root.geometry("800x800")
root.configure(bg="#0f172a")
# Style
style = ttk.Style()
style.theme_use("default")
style.configure("TProgressbar", thickness=30)
# Title
title = tk.Label(root, text="AI Resume Analyzer",text="Shows how well your resume matches our requrirement",
                 font=("Arial", 22, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=15)
# Role Frame
frame = tk.Frame(root, bg="#0f172a")
frame.pack()

tk.Label(frame, text="Select Job Role:",
         bg="#0f172a", fg="white",
         font=("Arial", 12)).grid(row=0, column=0, padx=5)

role_var = tk.StringVar()
role_dropdown = ttk.Combobox(frame, textvariable=role_var, width=25)
role_dropdown['values'] = ("Python Developer", "Data Scientist", "Web Developer")
role_dropdown.current(0)
role_dropdown.grid(row=0, column=1, padx=5)
# Input Box
tk.Label(root, text="Paste Your Resume below",
         bg="#0f172a", fg="white",
         font=("Arial Black", 14)).pack(pady=5)

text_box = tk.Text(root, height=9, width=100,
                   bg="#020617", fg="#ffffff",
                   insertbackground="white", bd=0)
text_box.pack(pady=10)
# Button
analyze_btn = tk.Button(root, text="Analyze Resume",
                        bg="#38bdf8", fg="black",
                        font=("Arial Black", 15, "bold"),
                        padx=10, pady=5,
                        command=run_analysis)
analyze_btn.pack(pady=10)
# Progress Section
progress_frame = tk.Frame(root, bg="#0f172a")
progress_frame.pack(pady=10)

progress = ttk.Progressbar(progress_frame, length=400, maximum=100)
progress.grid(row=0, column=0, padx=10)

score_label = tk.Label(progress_frame, text="0%",
                       bg="#0f172a", fg="white",
                       font=("Arial Black", 15, "bold"))
score_label.grid(row=0, column=1)
# Output Box
tk.Label(root, text="Analysis Result are displayed below",
         bg="#0f172a", fg="white",
         font=("Arial Black", 14)).pack(pady=5)

result_box = tk.Text(root, height=12, width=75,
                     bg="#020617", fg="white",
                     insertbackground="white", bd=0)
result_box.pack(pady=10)
# Color tags
result_box.tag_config("green", foreground="#22c55e")
result_box.tag_config("red", foreground="#ef4444")
result_box.config(state="disabled")
# Run App
root.mainloop()