# Restaurant Recommendation System

A machine learning-based recommendation system that suggests restaurants based on locality and similarity analysis. This project uses content-based filtering to recommend restaurants similar to a user's selected location.

## Project Overview

This restaurant recommendation system analyzes restaurant data and builds recommendations using similarity metrics. Users can select a locality and receive the top 5 most similar restaurant recommendations.

## Features

- **Content-Based Filtering**: Uses similarity scores to recommend restaurants
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Locality-Based Search**: Browse and select from available localities
- **Top 5 Recommendations**: Get the best matching restaurant recommendations

## Project Structure

```
├── main.py                          # Entry point for the recommendation engine
├── streamlitapp.py                  # Web interface built with Streamlit
├── Restaurant recommendation.ipynb  # Jupyter notebook for data analysis and model building
├── restaurants.csv                  # Raw restaurant data
├── restaurants_dict.pkl             # Pickled restaurant data dictionary
└── similarity.pkl                   # Pre-computed similarity matrix
```

## Files Description

### `streamlitapp.py`
The main web application that provides an interactive interface for users to select a locality and receive restaurant recommendations.

**Features:**
- Dropdown menu to select locality
- Button to trigger recommendations
- Display of top 5 recommended restaurants

### `main.py`
Core recommendation logic containing the `recomm()` function that:
1. Finds the index of the selected locality
2. Calculates similarity distances
3. Returns top 5 most similar restaurants

### `Restaurant recommendation.ipynb`
Jupyter Notebook containing the data preprocessing and model building pipeline:
- Data loading and exploration
- Data cleaning (lowercase conversion, duplicate removal, whitespace handling)
- Feature engineering (combining city, location, cuisine, rating, votes, cost)
- Similarity matrix computation

## Dependencies

- pandas
- numpy
- scikit-learn
- streamlit
- matplotlib
- pickle

## Installation

1. Clone or download this project
2. Install required dependencies:
```bash
pip install pandas numpy scikit-learn streamlit matplotlib
```

3. Ensure the following pickle files are in the project directory:
   - `restaurants_dict.pkl`
   - `similarity.pkl`

## Usage

### Running the Web Application

```bash
streamlit run streamlitapp.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Recommendation System

1. Select a locality from the dropdown menu
2. Click the "Recommend" button
3. View the top 5 recommended restaurants

## Data Processing

The system processes restaurant data through:
1. **Normalization**: Converting text to lowercase
2. **Deduplication**: Removing duplicate entries
3. **Cleaning**: Removing whitespace from relevant columns
4. **Feature Engineering**: Creating composite tags combining multiple attributes
5. **Similarity Calculation**: Computing cosine similarity between restaurant features

## How Recommendations Work

The recommendation algorithm:
1. Takes the selected locality as input
2. Retrieves the corresponding restaurant's index
3. Calculates similarity scores between the selected restaurant and all others
4. Returns the top 5 restaurants with the highest similarity scores (excluding the input restaurant itself)

## Requirements

- Python 3.7+
- All dependencies listed in `Dependencies` section

## Future Enhancements

- Collaborative filtering recommendations
- User ratings and feedback integration
- More detailed restaurant information display
- Advanced filtering options (cuisine type, price range, rating)
- Mobile-friendly interface improvements
- Recommendation reasons/explanations

## Author

Research Papers - Restaurant Recommendation System

## Notes

- The recommendation system uses pre-computed similarity matrices for performance
- Ensure all required pickle files are available before running the application
- The notebook can be used to rebuild the similarity matrices if new data is added
