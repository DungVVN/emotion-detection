# Emotion Detection Web Application

Author: Dinh Minh

A Flask web application using the IBM Watson NLP emotion prediction service to return anger, disgust, fear, joy, sadness and the dominant emotion.

Install: `python -m pip install -r requirements.txt`

Run: `python server.py`

Live Watson tests: `python -m unittest test_emotion_detection -v`

Static analysis: `python -m pylint server.py --persistent=n --disable=missing-module-docstring,missing-function-docstring`

The Watson endpoint must be reachable from the execution environment. Network failures are reported as service unavailable; they are not classified as emotions.

Submission evidence: code stages are in evidence/. Package import, Flask blank-input handling, and pylint 10.00/10 were verified locally. The error-handling screenshot was captured from the local application. Successful live Watson predictions and live emotion test results remain unverified because the service connection timed out from this machine.

The initial template and assignment reference came from `IBM-full-stack-software-developer-main/07-DevelopingAIApplicationswithPythonandFlask/Week-3/FinalProject/final-project-emb-ai` in the local course materials. The application code and interface were adapted for this submission.

Docstring style checks are disabled because this submission intentionally omits docstrings.
