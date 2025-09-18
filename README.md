# Log_Analysis_Script
### README: Log Analysis Tool

---

#### **Overview**
This Python tool analyzes server logs to:
- Count requests per IP.
- Identify the most accessed endpoint.
- Detect suspicious activity (failed login attempts exceeding a threshold).

Results are displayed in the console and saved in a CSV file in the `output` folder..

---

#### **Usage**
1. **Setup**: Place your log file in the project directory and set its path in `config.py`:
   ```python
   LOG_FILE_PATH = "sample.log"
   FAILED_LOGIN_THRESHOLD = 10
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Results**:
   - Console: Displays request counts, most accessed endpoint, and suspicious IPs.
   - CSV: Results saved in `output/log_analysis_results.csv`.

---

#### **Project Structure**
- `main.py`: Main script.
- `log_processor.py`: Log processing logic.
- `config.py`: Configurable settings.
- `output/`: Directory for saving CSV output.

---

#### **Notes**
- `output` folder is created automatically if missing.
- Requires Python's built-in libraries only.

--- 

Let me know if you need further clarification!!!!!
