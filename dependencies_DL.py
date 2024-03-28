import subprocess

def install_dependencies():
    dependencies = [
        'tensorflow==2.7.0',
        'torch==1.10.0',
        'keras==2.6.0',
        'numpy==1.21.5',
        'pandas==1.3.5',
        'matplotlib==3.5.1',
        'seaborn==0.11.2',
        'scikit-learn==1.0.1',
        'scipy==1.7.3',
        'opencv-python==4.5.3',
        'xgboost==1.5.1',
        'lightgbm==3.3.2',
        'scikit-image==0.18.3',
        'fastai==2.5.3',
        'transformers==4.12.2',
        'torchvision==0.11.1',
        'nltk==3.6.5',
        'spacy==3.2.1',
        'gensim==4.1.2',
        'pyttsx3==2.90',
        'SpeechRecognition==3.8.1',
        # Add more dependencies as needed
    ]

    subprocess.run(['pip', 'install'] + dependencies, check=True)

if __name__ == '__main__':
    install_dependencies()
