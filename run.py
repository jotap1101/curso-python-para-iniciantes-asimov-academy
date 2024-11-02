from streamlit.web import cli
import sys

sys.argv = ["streamlit", "run", "app.py"]

sys.exit(cli.main())
