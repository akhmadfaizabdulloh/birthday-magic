/* ==================================================
   GAME STATE
================================================== */

let currentDateCard = 0;

let currentMonthCard = 0;

let guessedDate = 0;

let guessedMonth = 0;


/* ==================================================
   DOM ELEMENTS
================================================== */

/*
 * Screens
 */

const homeScreen = document.querySelector("#home-screen");

const dateScreen = document.querySelector("#date-screen");

const monthScreen = document.querySelector("#month-screen");

const resultScreen = document.querySelector("#result-screen");


/*
 * Home
 */

const startButton = document.querySelector("#start-button");

const homeButton = document.querySelector("#home-button");


/*
 * Date game
 */

const dateTableTitle = document.querySelector(
    "#date-table-title"
);

const dateTable = document.querySelector(
    "#date-table"
);

const dateYesButton = document.querySelector(
    "#date-yes-button"
);

const dateNoButton = document.querySelector(
    "#date-no-button"
);


/*
 * Month game
 */

const monthTableTitle = document.querySelector(
    "#month-table-title"
);

const monthTable = document.querySelector(
    "#month-table"
);

const monthYesButton = document.querySelector(
    "#month-yes-button"
);

const monthNoButton = document.querySelector(
    "#month-no-button"
);


/*
 * Result
 */

const resultDate = document.querySelector(
    "#result-date"
);

const resultMonth = document.querySelector(
    "#result-month"
);


/* ==================================================
   SCREEN MANAGEMENT
================================================== */

function showScreen(screen) {

    /*
     * Sembunyikan semua screen terlebih dahulu.
     */

    homeScreen.hidden = true;
    dateScreen.hidden = true;
    monthScreen.hidden = true;
    resultScreen.hidden = true;


    /*
     * Tampilkan screen yang diminta.
     */

    screen.hidden = false;
}


/* ==================================================
   START GAME
================================================== */

function startGame() {

    /*
     * Reset state game.
     */

    currentDateCard = 0;

    currentMonthCard = 0;

    guessedDate = 0;

    guessedMonth = 0;


    /*
     * Tampilkan tabel tanggal pertama.
     */

    showScreen(dateScreen);

    renderDateCard();
}


/* ==================================================
   GENERATE DATE CARD
================================================== */

function generateDateNumbers(value) {

    const numbers = [];


    /*
     * Kita cek tanggal 1 - 31.
     *
     * Sebuah angka masuk ke tabel
     * apabila mempunyai bit/value tersebut.
     *
     * Contoh:
     *
     * value = 1
     *
     * 1  -> masuk
     * 2  -> tidak
     * 3  -> masuk
     * 4  -> tidak
     * 5  -> masuk
     *
     * dst.
     */

    for (let number = 1; number <= 31; number++) {

        if ((number & value) !== 0) {
            numbers.push(number);
        }
    }


    return numbers;
}


/* ==================================================
   RENDER DATE CARD
================================================== */

function renderDateCard() {

    const card = dateCards[currentDateCard];


    /*
     * Update judul tabel.
     */

    dateTableTitle.textContent = card.title;


    /*
     * Bersihkan tabel sebelumnya.
     */

    dateTable.innerHTML = "";


    /*
     * Generate angka untuk tabel.
     */

    const numbers = generateDateNumbers(card.value);


    /*
     * Masukkan angka ke dalam HTML.
     */

    numbers.forEach(number => {

        const cell = document.createElement("div");

        cell.classList.add("number-cell");

        cell.textContent = number;

        dateTable.appendChild(cell);
    });
}


/* ==================================================
   DATE ANSWER
================================================== */

function answerDate(answer) {

    const card = dateCards[currentDateCard];


    /*
     * Kalau user menjawab IYA,
     * tambahkan nilai kartu ke hasil.
     */

    if (answer === true) {

        guessedDate += card.value;
    }


    /*
     * Pindah ke tabel berikutnya.
     */

    currentDateCard++;


    /*
     * Kalau semua tabel tanggal sudah selesai,
     * lanjut ke game bulan.
     */

    if (currentDateCard >= dateCards.length) {

        /*
         * Jika hasil tanggal = 0,
         * berarti semua jawaban adalah TIDAK.
         */

        if (guessedDate === 0) {
            alert(
                "Pastikan tanggal lahir kamu ada di dalam tabel!"
            );

            guessedDate = 0;
            currentDateCard = 0;

            renderDateCard();
            return;
        }

        currentMonthCard = 0;

        showScreen(monthScreen);

        renderMonthCard();

        return;
    }


    /*
     * Kalau belum selesai,
     * tampilkan tabel berikutnya.
     */

    renderDateCard();
}



/* ==================================================
   RENDER MONTH CARD
================================================== */

function renderMonthCard() {

    const card = monthCards[currentMonthCard];


    /*
     * Update judul card.
     */

    monthTableTitle.textContent = card.title;


    /*
     * Bersihkan tabel sebelumnya.
     */

    monthTable.innerHTML = "";


    /*
     * Gunakan angka yang sudah
     * ditentukan di data.js.
     */

    card.numbers.forEach(number => {

        const cell = document.createElement("div");

        cell.classList.add("number-cell");

        cell.textContent = number;

        monthTable.appendChild(cell);
    });
}


/* ==================================================
   MONTH ANSWER
================================================== */

function answerMonth(answer) {

    const card = monthCards[currentMonthCard];


    /*
     * Kalau IYA,
     * tambahkan nilai kartu.
     */

    if (answer === true) {

        guessedMonth += card.value;
    }


    /*
     * Pindah ke tabel berikutnya.
     */

    currentMonthCard++;


    /*
     * Kalau semua tabel bulan selesai,
     * tampilkan hasil.
     */

    if (currentMonthCard >= monthCards.length) {


        if (guessedMonth === 12) {
            alert("Pastikan bulan lahir kamu ada di dalam tabel!");

            guessedMonth = 0;
            currentMonthCard = 0;

            renderMonthCard();
            return;
        }
        
        showResult();

        return;
    }


    /*
     * Kalau belum selesai,
     * tampilkan tabel berikutnya.
     */

    renderMonthCard();
}

function handleMonthAnswer(isYes) {
    const card = monthCards[currentMonthCard];

    if (isYes) {
        guessedMonth += card.value;
    }

    currentMonthCard++;

    if (currentMonthCard < monthCards.length) {
        renderMonthCard();
    } else {
        showResult();
    }
}

function getMonthName(month) {
    const months = [
        "Desember",
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember"
    ];

    return months[month] || "Desember";
}

/* ==================================================
   SHOW RESULT
================================================== */

function showResult() {

    if (guessedDate < 1 || guessedDate > 31) {
        alert("Tanggal tidak valid. Silakan coba lagi.");
        return;
    }

    resultDate.textContent = guessedDate;
    resultMonth.textContent = getMonthName(guessedMonth);

    showScreen(resultScreen);
}


/* ==================================================
   BACK TO HOME
================================================== */

function goHome() {

    /*
     * Reset game.
     */

    currentDateCard = 0;

    currentMonthCard = 0;

    guessedDate = 0;

    guessedMonth = 0;


    /*
     * Kembali ke Home.
     */

    showScreen(homeScreen);
}


/* ==================================================
   EVENT LISTENERS
================================================== */


/*
 * MULAI
 */

startButton.addEventListener(
    "click",
    startGame
);


/*
 * DATE — IYA
 */

dateYesButton.addEventListener(
    "click",
    () => answerDate(true)
);


/*
 * DATE — TIDAK
 */

dateNoButton.addEventListener(
    "click",
    () => answerDate(false)
);


/*
 * MONTH — IYA
 */

monthYesButton.addEventListener(
    "click",
    () => answerMonth(true)
);


/*
 * MONTH — TIDAK
 */

monthNoButton.addEventListener(
    "click",
    () => answerMonth(false)
);


/*
 * HOME
 */

homeButton.addEventListener(
    "click",
    goHome
);