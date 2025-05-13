const display = document.getElementById("display");
const buttons = document.querySelectorAll(".btn");
let input = "";

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const key = button.getAttribute("data-key");

    if (key === "C") {
      input = "";
      updateDisplay("0");
    } else if (key === "←") {
      input = input.slice(0, -1);
      updateDisplay(input || "0");
    } else if (key === "=") {
      try {
        const result = eval(input);
        updateDisplay(result);
        input = result.toString();
      } catch {
        updateDisplay("Error");
        input = "";
      }
    } else {
      if (input === "0" && !isNaN(key)) input = key;
      else input += key;
      updateDisplay(input);
    }
  });
});

function updateDisplay(value) {
  display.textContent = value;
}
