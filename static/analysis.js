// JavaScript function to calculate counts and rating
function calculateCountsAndRating() {
    // Get the reviews data from the server
    const reviewsData = JSON.parse("{{ reviews|tojson|safe }}");

    if (!reviewsData || reviewsData.length === 0) {
        return; // No reviews to calculate
    }

    const positiveReviews = reviewsData.filter(
        (review) => review[1] === "Positive"
    );
    const negativeReviews = reviewsData.filter(
        (review) => review[1] === "Negative"
    );
    const neutralReviews = reviewsData.filter(
        (review) => review[1] === "Neutral"
    );
    const totalReviews = reviewsData.length;

    // Calculate the rating based on the number of positive reviews
    const rating = ((positiveReviews.length / totalReviews) * 5).toFixed(2); // Assuming 5 as the maximum rating

    // Update the placeholders in the HTML
    document.getElementById("positive-count").textContent =
        positiveReviews.length;
    document.getElementById("negative-count").textContent =
        negativeReviews.length;
    document.getElementById("neutral-count").textContent = neutralReviews.length;
    document.getElementById("total-reviews").textContent = totalReviews;
    document.getElementById("rating").textContent = rating;
}

// Call the function when the page loads
window.addEventListener("load", calculateCountsAndRating);
