const cards = [
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],

    [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],

    [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],

    [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],

    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
];

let currentCard = 0;
let guessedDate = 0;


// Elements
const startButton = document.querySelector("#start-button");

const cardContainer = document.querySelector("#card-container");
const cardTitle = document.querySelector("#card-title");
const card = document.querySelector("#card");

const yesButton = document.querySelector("#yes-button");
const noButton = document.querySelector("#no-button");

const result = document.querySelector("#result");
const resultText = document.querySelector("#result-text");

const restartButton = document.querySelector("#restart-button");


// Start game
startButton.addEventListener("click", startGame);


function startGame() {
    currentCard = 0;
    guessedDate = 0;

    startButton.hidden = true;
    result.hidden = true;
    cardContainer.hidden = false;

    showCard();
}


// Show current card
function showCard() {
    const currentNumbers = cards[currentCard];

    cardTitle.textContent = `Card ${currentCard + 1}`;

    card.textContent = currentNumbers.join("    ");
}


// User answered YES
yesButton.addEventListener("click", () => {
    guessedDate += 2 ** currentCard;

    nextCard();
});


// User answered NO
noButton.addEventListener("click", () => {
    nextCard();
});


// Move to next card
function nextCard() {
    currentCard++;

    if (currentCard >= cards.length) {
        showResult();
        return;
    }

    showCard();
}


// Show result
function showResult() {
    cardContainer.hidden = true;
    result.hidden = false;

    resultText.textContent = guessedDate;
}


// Restart
restartButton.addEventListener("click", () => {
    result.hidden = true;
    startButton.hidden = false;
});