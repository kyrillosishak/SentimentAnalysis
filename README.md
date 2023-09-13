# Sentiment Analysis Project README

## Project Overview

This repository contains the code and documentation for a sentiment analysis project focused on analyzing Amazon product reviews. The project aims to classify customer sentiments (positive or negative) from the text of product reviews.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Data Collection](#data-collection)
- [Web Scraping](#web-scraping)
- [Data Preprocessing](#data-preprocessing)
- [Model Development](#model-development)
- [Model Evaluation](#model-evaluation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To run this project, you will need the following:

- Python 3.6+
- Libraries listed in `requirements.txt`

You can install the required libraries using pip:

```shell
pip install -r requirements.txt
## Data Collection

The project collects Amazon product reviews for sentiment analysis. We selected specific product categories and employed web scraping techniques to retrieve review data. The collected dataset serves as the basis for training and evaluating sentiment analysis models.

## Web Scraping

We utilized Selenium, a web automation and testing tool, for web scraping. Selenium allowed us to interact with Amazon product pages programmatically, extract review content, and store the data for analysis. Ethical considerations, rate limiting, and data preprocessing were implemented to ensure responsible web scraping.

## Data Preprocessing

Raw scraped data often requires preprocessing to ensure its suitability for sentiment analysis. Data preprocessing steps, including text cleaning, formatting, and tokenization, were applied to enhance the quality of the collected reviews.

## Model Development

The project includes the development of sentiment analysis models, employing two primary approaches:

- **Logistic Regression:** A traditional machine learning model.
- **Long Short-Term Memory (LSTM):** A deep learning model.

The models were trained and evaluated on the preprocessed review data, and their performance was compared.

## Model Evaluation

Model evaluation metrics include accuracy, precision, recall, F1-score, and confusion matrices. We compare the performance of Logistic Regression and LSTM models and discuss their strengths and weaknesses.
## Results
- **Logistic Regression:** Accuracy : 83.9 precent
- **Long Short-Term Memory (LSTM):** Accuracy : 93 precent
