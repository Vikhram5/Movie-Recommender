document.addEventListener("DOMContentLoaded", function () {
    const reviewContents = document.querySelectorAll(".review-content");

    reviewContents.forEach(content => {
        content.addEventListener("click", function () {
            this.classList.toggle("expanded");
        });
    });
});

