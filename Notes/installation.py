# ---------- GLOBAL INSTALL ----------  You only need to do this once ever (technically)
    # this is a global install for the pipenv package

    pip install pipenv


# ---------- VIRTUAL ENVIRONMENT ----------
    # **Do this in every Project (Aka Assignment, AKA repository)Folder**
    
    # ---------- STEP ONE INSTALL FLASK AND VIRTUAL ENVIRONMENT----------
    pipenv install flask PyMySQL

    # (EVENTUALLY IT WILL BE pipenv install flask PyMySQL flask-bcrypt)

    # ---------- STEP TWO - ACTIVATE VIRTUAL ENVIRONMENT ----------
    pipenv shell


# RUN YOUR SERVER:

python server.py 
# in some cases for macs, you might need python3 server.py