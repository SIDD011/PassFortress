# 🔐 PassFortress — Password Generator & Strength Checker


A Python-based cybersecurity utility that generates secure random passwords and evaluates their strength using entropy calculations and estimated brute-force crack times.

This project demonstrates practical understanding of password security, entropy concepts, and defensive security best practices.

---

## 🎯 Project Objective

- Generate strong random passwords  
- Measure password entropy  
- Classify password strength  
- Estimate brute-force crack time at different attack speeds  
- Save results to CSV for analysis  

---

## 🛠 Tools & Technology

- Python 3.x  
- Standard Python Libraries  
  - random  
  - string  
  - math  
  - csv  

---

## 🔎 Features

- Generate passwords using:
  - Lowercase letters  
  - Uppercase letters  
  - Numbers  
  - Symbols  

- Calculate password entropy (bits)  
- Strength classification:
  - Weak  
  - Moderate  
  - Strong  
  - Very Strong  

- Crack-time estimation for:
  - 1e3 guesses/sec  
  - 1e6 guesses/sec  
  - 1e9 guesses/sec  
  - 1e12 guesses/sec  

- Export results to CSV file  

---

## 📂 Project Structure

Password-Generator/

│

├── src/

│ └── password_generator.py

│

├── outputs/

│ └── password_strength_results.csv

│

└── README.md

yaml
Copy code

---

## ▶ How To Run

cd src
python password_generator.py

yaml
Copy code

Enter password length when prompted.

---

## 📊 Sample Output

Generated Password: mv!b^8YHc08F
Entropy: 78.66
Strength: Strong

Crack Time Estimates:
1e3/sec : 15143032414920 years
1e6/sec : 15143032414 years
1e9/sec : 15143032 years
1e12/sec: 15143 years

Saved to password_strength_results.csv

yaml
Copy code

---

## 📄 Output File

Results are saved in:

outputs/password_strength_results.csv

yaml
Copy code

This file contains:

- Password  
- Length  
- Entropy  
- Strength  
- Crack-time estimates  

---

## 📚 Learning Outcomes

- Understanding password entropy  
- Secure password generation  
- Brute-force attack concepts  
- Python scripting for security automation  
- Data logging using CSV  

---

## 🏁 Conclusion

This project demonstrates practical defensive security skills related to password hygiene and cryptographic strength analysis, useful for SOC Analyst, Blue Team, and Cybersecurity Analyst roles.

---
