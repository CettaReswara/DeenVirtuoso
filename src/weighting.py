import numpy as np
import scipy.stats as stats

def calculate_weight():
    # Calculate mean and standard deviation of ratings for each factor
    factor_1_ratings = tm.get_ratings("./data/twitter_dataset.csv")
    factor_2_ratings = tm.get_ratings("./data/dummy_tweets.csv")
    mean_rating_factor_1 = np.mean(factor_1_ratings)
    std_rating_factor_1 = np.std(factor_1_ratings)
    mean_rating_factor_2 = np.mean(factor_2_ratings)
    std_rating_factor_2 = np.std(factor_2_ratings)

    # Define the weight calculation function for each factor
    def calculate_weight_factor_1(rating):
        z_score = (rating - mean_rating_factor_1) / std_rating_factor_1
        weight = stats.norm.pdf(z_score)
        return weight

    def calculate_weight_factor_2(rating):
        z_score = (rating - mean_rating_factor_2) / std_rating_factor_2
        weight = stats.norm.pdf(z_score)
        return weight

    # Calculate weights for each factor
    weights_factor_1 = [calculate_weight_factor_1(rating) for rating in factor_1_ratings]
    weights_factor_2 = [calculate_weight_factor_2(rating) for rating in factor_2_ratings]

    # Combine the weights using a linear combination
    stopping_criteria = False
    weights_constant_1 = 0
    weights_constant_2 = 1
    while not stopping_criteria:
        combined_weights = weights_factor_1 * np.array(weights_factor_1) + weights_constant_2 * np.array(weights_factor_2)

        # Normalize the combined weights
        normalized_weights = combined_weights / np.sum(combined_weights)

        # Verify that the weights follow a normal distribution  
        _, p_value = stats.normaltest(normalized_weights)

        if p_value > 0.05:
            stopping_criteria = True
        else:
            weights_constant_1 += 0.1
            weights_constant_2 -= 0.1

    # Print the results
#    print("Mean rating (Factor 1):", mean_rating_factor_1)
#    print("Weights constant (Factor 1):", weights_constant_1)
#    print("Standard deviation of rating (Factor 1):", std_rating_factor_1)
#    print("Mean rating (Factor 2):", mean_rating_factor_2)
#    print("Standard deviation of rating (Factor 2):", std_rating_factor_2)
#    print("Weights constant (Factor 2):", weights_constant_2)
#    print("Combined weights:", combined_weights)
#    print("Normalized weights:", normalized_weights)
#    print("Is the weight distribution normal?", p_value > 0.05)

    # Return weights constant for each factor
    return weights_constant_1, weights_constant_2
