# Spam Detection with FastAPI and Machine Learning 📧

Welcome to the **Spam Detection** project! This project uses machine learning to classify emails or messages as either "spam" or "ham" (not spam). The model is integrated into a FastAPI web application, allowing users to input text and receive real-time predictions. The project uses **scikit-learn** for machine learning and **FastAPI** for building the web interface.

---

## Features

- **Real-Time Prediction**: Users can input text and receive instant predictions.
- **Machine Learning Model**: Uses a Random Forest Classifier trained on a spam dataset.
- **Text Preprocessing**: Includes tokenization, stopword removal, and stemming.
- **Interactive Web Interface**: Built with FastAPI for a seamless user experience.

---

## How It Works

1. **User Input**: Users input text via a web form or API request.
2. **Text Preprocessing**: The input text is preprocessed (tokenized, stopwords removed, and stemmed).
3. **Feature Extraction**: The preprocessed text is transformed into numerical features using a bag-of-words model.
4. **Prediction**: The features are passed to the machine learning model, which predicts whether the text is spam or ham.
5. **Result Display**: The prediction result is returned to the user.

---

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- FastAPI
- scikit-learn
- pandas
- numpy
- uvicorn
- nltk

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/spam-detection.git
   cd spam-detection
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data**:
   ```bash
   python -m nltk.downloader punkt stopwords
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn app:app --reload
   ```

5. **Open the application**:
   Visit `http://localhost:8000` in your browser.

---

## Usage

1. Open the web application in your browser.
2. Input the text you want to classify.
3. Click the "Predict" button to receive the prediction result.

---

## API Endpoint

You can also interact with the model programmatically using the `/predict/` endpoint:

### Request
- **Method**: POST
- **URL**: `http://localhost:8000/predict/`
- **Body**:
  ```json
  {
    "text": "Your input text here"
  }
  ```

### Response
- **Success**:
  ```json
  {
    "prediction": "ham"
  }
  ```
- **Error**:
  ```json
  {
    "detail": "Error message"
  }
  ```

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [scikit-learn](https://scikit-learn.org/) for the machine learning model.
- [nltk](https://www.nltk.org/) for text preprocessing.
- [pandas](https://pandas.pydata.org/) for data manipulation.
- [numpy](https://numpy.org/) for numerical computations.

---

Detect spam messages with ease using this Spam Detection project! 🚀📧
