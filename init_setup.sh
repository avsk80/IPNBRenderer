echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8..........."
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "Installing requirements.txt in dev"
pip3 install -r requirements_dev.txt
echo [$(date)]: "END"
