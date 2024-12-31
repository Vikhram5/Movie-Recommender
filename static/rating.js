$(document).ready(function () {
  // Count positive, negative, and neutral reviews
  var positiveCount = 0;
  var negativeCount = 0;
  var neutralCount = 0;

  // Loop through each row in the reviews table
  $(".reviews-table tbody tr").each(function () {
    var sentiment = $(this).find("td:last-child").text();

    // Update counts based on sentiment value
    if (sentiment === "Positive") {
      positiveCount++;
    } else if (sentiment === "Negative") {
      negativeCount++;
    } else if (sentiment === "Neutral") {
        
      neutralCount++;
    }
  });

  // Display the counts
  $("#positive-count").text(positiveCount);
  $("#negative-count").text(negativeCount);
  $("#neutral-count").text(neutralCount);

  // Calculate and display the overall rating
  var totalReviews = positiveCount + negativeCount + neutralCount;
  var overallRating =
    (positiveCount * 5 + neutralCount * 3 + negativeCount * 1) / totalReviews;
  $("#overall-rating").text(overallRating.toFixed(2));
});
