# LimitedKwargs

`LimitedKwargs` is a lightweight Python class designed to accept only a predefined set of keyword arguments and map them to custom internal keys. It provides input validation, key transformation, and user-friendly feedback for incorrect usage.

---

## 🚀 Features

- ✅ Accepts only specific keyword arguments (`a` through `f`)
- 🔄 Maps valid keys to internal keys (`g` through `l`)
- ⚠️ Warns about invalid keys and ignores them
- 🧩 Useful for data validation, configuration objects, or API wrappers

---

## 📦 Installation

No installation required. Just copy the class into your Python project.

---

## 🛠️ How It Works

- The class defines a set of valid keys: `a`, `b`, `c`, `d`, `e`, `f`
- When initialized, it checks if all provided keyword arguments are valid
- Invalid keys are reported and ignored
- Valid keys are mapped to internal keys:  
  - `a` → `g`  
  - `b` → `h`  
  - `c` → `i`  
  - `d` → `j`  
  - `e` → `k`  
  - `f` → `l`

---

## 📄 Example Usage

```python
from limited_kwargs import LimitedKwargs

# Valid and invalid keys
obj = LimitedKwargs(a=42, b="hello", x="invalid", c=[1, 2, 3])

# Access the internal dictionary
print(obj.dictionary)
# Output:
#
# Invalid key(s). These will be ignored:
#         - x
# Type LimitedKwargs.VALID_KEYS for valid keys.
# {
#     'g': 42,
#     'h': 'hello',
#     'i': [1, 2, 3]
# }
```
---
## 💡 Possible Use Cases
* Configuration objects with strict parameter control
* Wrappers for APIs that only accept specific fields
* Data sanitization before serialization (e.g., JSON)
* Mapping user input to internal system keys

---

## 📜 License
This code is free to use, modify, and distribute.

---
## 📁 File Structure
If you want to use this as a module:
```plaintext
your_project/
│
├── limited_kwargs.py   # Contains the LimitedKwargs class
├── README.md           # You're reading it!
└── main.py             # Your application logic
```

---

## 🤝 Contributing
Feel free to fork, improve, or adapt the class to your needs. Pull requests and suggestions are welcome!
