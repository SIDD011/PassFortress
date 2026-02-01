

\# Password Generator \& Strength Checker 🔐



A Python-based tool that generates secure random passwords and evaluates their strength using entropy and estimated brute-force crack times.



\## 📌 Features

\- Generate random passwords with:

&nbsp; - Uppercase letters

&nbsp; - Lowercase letters

&nbsp; - Numbers

&nbsp; - Symbols



--



\- Calculate password entropy (bits)

\- Classify strength:

&nbsp; - Weak

&nbsp; - Moderate

&nbsp; - Strong

&nbsp; - Very Strong

--

\- Estimate crack time at:

&nbsp; - 1e3 guesses/sec

&nbsp; - 1e6 guesses/sec

&nbsp; - 1e9 guesses/sec

&nbsp; - 1e12 guesses/sec

\- Save results to CSV file



---



\## 📂 Project Structure







Password-Generator/

│

├── src/

│ └── password\_generator.py

│

├── outputs/

│ └── password\_strength\_results.csv

│

└── README.md





---



\## ▶ How To Run







cd src

python password\_generator.py





Enter password length when prompted.



---



\## 🛠 Requirements



\- Python 3.x



Check version:







python --version





---



\## 📊 Output Example







Generated Password: mv!b^8YHc08F

Entropy: 78.66

Strength: Strong

1e3/sec: 15143032414920 years

1e6/sec: 15143032414 years

1e9/sec: 15143032 years

1e12/sec: 15143 years





---



\## 🚀 Author

Siddhesh Patil

