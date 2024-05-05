#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import ttk, messagebox
import random


class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker and Goal Setter")
        
        self.user_profile = {
            "name": "",
            "age": 0,
            "weight": 0,
            "height": 0,
            "fitness_goal": "",
            "activity_level": "",
            "calories_consumed": 0,
            "calories_burned": 0,
            "workout_schedule": []
        }
        
        self.name_label = ttk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.age_label = ttk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=2, column=0, padx=5, pady=5)
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.height_label = ttk.Label(root, text="Height (m):")
        self.height_label.grid(row=3, column=0, padx=5, pady=5)
        self.height_entry = ttk.Entry(root)
        self.height_entry.grid(row=3, column=1, padx=5, pady=5)
        
        self.fitness_goal_label = ttk.Label(root, text="Fitness Goal:")
        self.fitness_goal_label.grid(row=4, column=0, padx=5, pady=5)
        self.fitness_goal_combo = ttk.Combobox(root, values=["Weight Loss", "Muscle Gain", "Maintenance"])
        self.fitness_goal_combo.grid(row=4, column=1, padx=5, pady=5)
        
        self.save_profile_button = ttk.Button(root, text="Save Profile", command=self.save_profile)
        self.save_profile_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        self.track_progress_button = ttk.Button(root, text="Track Progress", command=self.track_progress)
        self.track_progress_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        
        self.fitness_goal_button = ttk.Button(root, text="Set Fitness Goal", command=self.set_fitness_goal)
        self.fitness_goal_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        
        self.motivational_messages = [
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
            "The only bad workout is the one that didn't happen.",
            "Your body can stand almost anything. It's your mind that you have to convince.",
            "The only way to do great work is to love what you do.",
            "Success is walking from failure to failure with no loss of enthusiasm."
        ]
    
    def save_profile(self):
        self.user_profile["name"] = self.name_entry.get()
        self.user_profile["age"] = int(self.age_entry.get())
        self.user_profile["weight"] = float(self.weight_entry.get())
        self.user_profile["height"] = float(self.height_entry.get())
        self.user_profile["fitness_goal"] = self.fitness_goal_combo.get()
        messagebox.showinfo("Profile Saved", "Your profile has been saved successfully!")
    
    def track_progress(self):
        if self.user_profile["name"] == "":
            messagebox.showerror("Error", "Please save your profile first!")
            return
        
        progress_summary = self.generate_progress_summary()
        messagebox.showinfo("Progress Summary", progress_summary)
        
        self.show_motivational_message()
    
    def generate_progress_summary(self):
        bmi = self.calculate_bmi(self.user_profile["weight"], self.user_profile["height"])
        fitness_level = self.determine_fitness_level(bmi, self.user_profile["age"])
        
        progress_summary = (
            f"Name: {self.user_profile['name']}\n"
            f"Age: {self.user_profile['age']}\n"
            f"Weight: {self.user_profile['weight']} kg\n"
            f"Height: {self.user_profile['height']} m\n"
            f"Fitness Goal: {self.user_profile['fitness_goal']}\n"
            f"BMI: {bmi:.2f}\n"
            f"Fitness Level: {fitness_level}"
        )
        return progress_summary
    
    def show_motivational_message(self):
        message = random.choice(self.motivational_messages)
        messagebox.showinfo("Motivational Message", message)
    
    def set_fitness_goal(self):
        fitness_goal = self.fitness_goal_combo.get()
        messagebox.showinfo("Fitness Goal Set", f"Your fitness goal is set to: {fitness_goal}")
    
    @staticmethod
    def calculate_bmi(weight_kg, height_m):
        return weight_kg / (height_m ** 2)
    
    @staticmethod
    def determine_fitness_level(bmi, age):
        if age < 18:
            return "Age under 18, consult a doctor"
        elif 18 <= age <= 24:
            return "Fit" if 18.5 <= bmi < 25 else "Underfit" if bmi < 18.5 else "Overfit"
        elif 25 <= age <= 34:
            return "Fit" if 18.5 <= bmi < 25 else "Underfit" if bmi < 18.5 else "Overfit"
        else:
            return "Fit" if 20 <= bmi < 25 else "Underfit" if bmi < 20 else "Overfit"


root = tk.Tk()
app = FitnessApp(root)
root.mainloop()


# In[ ]:





# In[ ]:




