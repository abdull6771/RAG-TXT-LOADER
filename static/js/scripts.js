document
  .querySelector('form[method="POST"][enctype="multipart/form-data"]')
  .addEventListener("submit", function (e) {
    const fileInput = this.querySelector('input[type="file"]');
    const file = fileInput.files[0];
    if (file && !file.name.endsWith(".txt")) {
      e.preventDefault();
      alert("Please upload a .txt file.");
    } else {
      const btn = this.querySelector("#upload-btn");
      btn.disabled = true;
      btn.querySelector(".upload-text").classList.add("hidden");
      btn.querySelector(".loading-text").classList.remove("hidden");
    }
  });

document
  .querySelector('form[method="POST"]:not([enctype])')
  .addEventListener("submit", function (e) {
    const questionInput = this.querySelector('input[name="question"]');
    if (questionInput.value.trim().length < 3) {
      e.preventDefault();
      alert("Please enter a valid question (at least 3 characters).");
    } else {
      const btn = this.querySelector("button[type='submit']");
      btn.disabled = true;
      btn.querySelector(".ask-text").classList.add("hidden");
      btn.querySelector(".loading-text").classList.remove("hidden");
    }
  });
