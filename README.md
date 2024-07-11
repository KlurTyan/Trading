## Installation
1. Make sure that Python 3.6 or higher and Git are installed on your computer.

2. Clone the repository:
``` bash
git clone https://github.com/KlurTyan/Trading.git
```

3. Change the directory:
``` bash
cd Trading
```

4. Create a virtual environment (recommended):
``` bash
python -m venv venv
```

5. Activate it:
* Windows:
``` bash
venv\Scripts\activate
```

* Linux/macOS:
``` bash
source venv/bin/activate
```

6. Install dependencies:
``` bash
pip install -r requirements.txt
```

## Usage
Run application with command:
``` bash
uvicorn src.app:main --reload
```
or
``` bash
cd src
uvicorn app:main --reload
```