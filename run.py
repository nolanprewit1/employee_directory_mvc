### IMPORT REQUIRED PYTHON MODULES ###
import json
from project import app

### START THE APP ###    
if __name__ == '__main__':    
    app.run(host="0.0.0.0",port="8080")