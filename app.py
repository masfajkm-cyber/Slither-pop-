import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SlitherPop",
    page_icon="🐍",
    layout="centered"
)

components.html("""
<!DOCTYPE html>
<html>
<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #f2f3f5;
    font-family: Arial, sans-serif;
    text-align: center;
    color: #252a31;
    overscroll-behavior: none;
    user-select: none;
}


/* =========================
   TITLE
========================= */

.title {
    font-size: 32px;
    font-weight: 900;
    margin-top: 8px;
    color: #252a31;
    letter-spacing: -1px;
}

.by {
    font-size: 13px;
    font-weight: 600;
    color: #858b94;
    margin-bottom: 12px;
}


/* =========================
   CUSTOMIZE BUTTON
========================= */

.customize {
    border: 1px solid #d5d8dc;
    background: #ffffff;
    color: #252a31;
    border-radius: 14px;
    padding: 10px 20px;
    font-size: 15px;
    font-weight: 800;
    cursor: pointer;
    margin-bottom: 10px;
    box-shadow: 0 2px 7px rgba(0,0,0,.05);
}

.customize:active {
    transform: scale(.96);
}


/* =========================
   CUSTOMIZATION PANEL
========================= */

.custom-panel {
    display: none;
    max-width: 390px;
    margin: 0 auto 13px auto;
    background: #ffffff;
    border: 1px solid #d8dbe0;
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,.08);
}

.custom-panel.open {
    display: block;
}

.custom-title {
    font-size: 14px;
    font-weight: 800;
    color: #555b64;
    margin-bottom: 9px;
}

.choice-row {
    display: flex;
    justify-content: center;
    gap: 7px;
    flex-wrap: wrap;
}

.choice {
    border: 2px solid #e0e2e5;
    background: #f7f8f9;
    color: #333840;
    border-radius: 12px;
    padding: 7px 10px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
}

.choice.selected {
    border-color: #303640;
    background: #e7e9ec;
}


/* =========================
   SCORE CARD
========================= */

.score-card {
    width: min(90vw, 360px);
    margin: 8px auto 10px auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    border: 1px solid #dfe2e6;
    border-radius: 15px;
    padding: 10px 15px;
    box-shadow: 0 3px 10px rgba(0,0,0,.05);
}

.score {
    font-size: 18px;
    font-weight: 900;
    color: #303640;
}

.speed {
    font-size: 12px;
    font-weight: 700;
    color: #7a8088;
}


/* =========================
   GAME
========================= */

.game-wrap {
    position: relative;
    width: min(90vw, 360px);
    margin: auto;
}

canvas {
    width: 100%;
    height: auto;
    aspect-ratio: 1 / 1;
    background: #ffffff;
    border: 4px solid #303640;
    border-radius: 22px;
    display: block;
    margin: auto;
    touch-action: none;
    box-shadow: 0 7px 20px rgba(0,0,0,.10);
}


/* =========================
   CONTROLS
========================= */

.controls {
    width: 225px;
    margin: 15px auto 12px auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}

.control {
    height: 58px;
    border: 1px solid #d1d5da;
    border-radius: 17px;
    background: #ffffff;
    color: #303640;
    font-size: 25px;
    font-weight: bold;
    touch-action: manipulation;
    box-shadow: 0 3px 8px rgba(0,0,0,.06);
}

.control:active {
    transform: scale(.91);
    background: #e6e8eb;
}

.empty {
    visibility: hidden;
}


/* =========================
   RESTART
========================= */

.restart {
    border: none;
    border-radius: 15px;
    background: #303640;
    color: white;
    padding: 12px 29px;
    font-size: 16px;
    font-weight: 900;
    cursor: pointer;
    margin-bottom: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,.12);
}

.restart:active {
    transform: scale(.95);
}


/* =========================
   GAME OVER BUTTON
========================= */

.game-over-button {
    display: none;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border: none;
    border-radius: 14px;
    background: #303640;
    color: white;
    padding: 11px 21px;
    font-size: 15px;
    font-weight: 800;
    cursor: pointer;
}

.game-over-button.show {
    display: block;
}

</style>

</head>

<body>


<div class="title">SlitherPop</div>

<div class="by">by Masfa</div>


<button class="customize" id="customize">
    ⚙️ Customize
</button>


<div class="custom-panel" id="customPanel">

    <div class="custom-title">
        🐍 Snake Color
    </div>

    <div class="choice-row">

        <button class="choice selected"
                data-color="#d94f7d">
            🩷 Pink
        </button>

        <button class="choice"
                data-color="#e53935">
            ❤️ Red
        </button>

        <button class="choice"
                data-color="#2196f3">
            💙 Blue
        </button>

        <button class="choice"
                data-color="#4caf50">
            💚 Green
        </button>

        <button class="choice"
                data-color="#8e44ad">
            💜 Purple
        </button>

        <button class="choice"
                data-color="#20242a">
            🖤 Black
        </button>

    </div>

    <br>

    <div class="custom-title">
        🍎 Food
    </div>

    <div class="choice-row">

        <button class="choice food selected"
                data-food="🍎">
            🍎 Apple
        </button>

        <button class="choice food"
                data-food="🍓">
            🍓 Berry
        </button>

        <button class="choice food"
                data-food="🍒">
            🍒 Cherry
        </button>

        <button class="choice food"
                data-food="🍕">
            🍕 Pizza
        </button>

        <button class="choice food"
                data-food="🍩">
            🍩 Donut
        </button>

        <button class="choice food"
                data-food="🍉">
            🍉 Melon
        </button>

    </div>

</div>


<!-- SCORE -->

<div class="score-card">

    <div class="score" id="score">
        🏆 Score: 0
    </div>

    <div class="speed" id="speed">
        🐢 Slow
    </div>

</div>


<!-- GAME -->

<div class="game-wrap">

    <canvas
        id="game"
        width="360"
        height="360">
    </canvas>

    <button
        class="game-over-button"
        id="gameOverRestart">
        🔄 Restart
    </button>

</div>


<!-- TOUCH CONTROLS -->

<div class="controls">

    <div class="empty"></div>

    <button class="control" id="up">
        ⬆️
    </button>

    <div class="empty"></div>

    <button class="control" id="left">
        ⬅️
    </button>

    <button class="control" id="down">
        ⬇️
    </button>

    <button class="control" id="right">
        ➡️
    </button>

</div>


<button class="restart" id="restart">
    🔄 Restart Game
</button>


<script>

const canvas = document.getElementById("game");

const ctx = canvas.getContext("2d");


/* =========================
   GAME SETTINGS
========================= */

const grid = 18;
const cell = 20;


/* =========================
   GAME VARIABLES
========================= */

let snake;

let direction;

let nextDirection;

let food;

let foodEmoji = "🍎";

let snakeColor = "#d94f7d";

let score = 0;

let gameOver = false;


/*
   START SLOW.
   Smaller number = faster.
*/

let gameSpeed = 220;

let gameTimer;


/* =========================
   RESTART
========================= */

function restart() {

    snake = [

        {x: 9, y: 9},
        {x: 8, y: 9},
        {x: 7, y: 9},
        {x: 6, y: 9}

    ];


    direction = {
        x: 1,
        y: 0
    };


    nextDirection = {
        x: 1,
        y: 0
    };


    score = 0;

    gameOver = false;

    gameSpeed = 220;


    document.getElementById("score").textContent =
        "🏆 Score: 0";


    document.getElementById("speed").textContent =
        "🐢 Slow";


    document
        .getElementById("gameOverRestart")
        .classList.remove("show");


    createFood();

    draw();


    startGameLoop();

}


/* =========================
   GAME LOOP
========================= */

function startGameLoop() {

    clearInterval(gameTimer);


    gameTimer = setInterval(

        function() {

            moveSnake();

            draw();

        },

        gameSpeed

    );

}


/* =========================
   FOOD
========================= */

function createFood() {

    let valid = false;


    while (!valid) {

        food = {

            x: Math.floor(Math.random() * grid),

            y: Math.floor(Math.random() * grid)

        };


        valid = true;


        for (let part of snake) {

            if (

                part.x === food.x &&
                part.y === food.y

            ) {

                valid = false;

                break;

            }

        }

    }

}


/* =========================
   DIRECTION
========================= */

function changeDirection(x, y) {

    /*
       Prevent instant opposite turns.
       This makes controls smoother.
    */

    if (

        direction.x + x === 0 &&
        direction.y + y === 0

    ) {

        return;

    }


    nextDirection = {

        x: x,
        y: y

    };

}


/* =========================
   MOVE
========================= */

function moveSnake() {

    if (gameOver) {

        return;

    }


    direction = nextDirection;


    const head = {

        x: snake[0].x + direction.x,

        y: snake[0].y + direction.y

    };


    /* =========================
       WALL COLLISION
    ========================= */

    if (

        head.x < 0 ||
        head.x >= grid ||
        head.y < 0 ||
        head.y >= grid

    ) {

        gameOver = true;


        clearInterval(gameTimer);


        document
            .getElementById("gameOverRestart")
            .classList.add("show");


        return;

    }


    /*
       NO SELF COLLISION.
       THE SNAKE CAN CROSS ITSELF.
    */

    snake.unshift(head);


    /* =========================
       FOOD
    ========================= */

    if (

        head.x === food.x &&
        head.y === food.y

    ) {

        score++;


        document.getElementById("score").textContent =
            "🏆 Score: " + score;


        createFood();


        /*
           Gradually get faster.

           It starts at 220ms.
           Every few points it gets
           slightly faster.

           It never becomes crazy fast.
        */

        if (score % 5 === 0) {

            gameSpeed = Math.max(
                150,
                gameSpeed - 10
            );


            if (gameSpeed > 195) {

                document.getElementById("speed").textContent =
                    "🐢 Slow";

            }

            else if (gameSpeed > 170) {

                document.getElementById("speed").textContent =
                    "🏃 Medium";

            }

            else {

                document.getElementById("speed").textContent =
                    "🔥 Fast";

            }


            startGameLoop();

        }

    }

    else {

        snake.pop();

    }

}


/* =========================
   GRID
========================= */

function drawGrid() {

    ctx.strokeStyle = "#e4e7ea";

    ctx.lineWidth = 1;


    for (let i = 0; i <= grid; i++) {

        const position = i * cell;


        /* Vertical */

        ctx.beginPath();

        ctx.moveTo(position, 0);

        ctx.lineTo(
            position,
            canvas.height
        );

        ctx.stroke();


        /* Horizontal */

        ctx.beginPath();

        ctx.moveTo(0, position);

        ctx.lineTo(
            canvas.width,
            position
        );

        ctx.stroke();

    }

}


/* =========================
   DRAW SNAKE
========================= */

function drawSnake() {

    snake.forEach(

        function(part, index) {

            const x =
                part.x * cell + 10;

            const y =
                part.y * cell + 10;


            /* =========================
               BODY
            ========================= */

            if (index !== 0) {

                /*
                   Small shadow.
                */

                ctx.fillStyle =
                    "rgba(0,0,0,.10)";


                ctx.beginPath();

                ctx.arc(
                    x + 1,
                    y + 2,
                    8,
                    0,
                    Math.PI * 2
                );

                ctx.fill();


                /*
                   Body.
                */

                ctx.fillStyle =
                    snakeColor;


                ctx.beginPath();

                ctx.arc(
                    x,
                    y,
                    8,
                    0,
                    Math.PI * 2
                );

                ctx.fill();

            }


            /* =========================
               HEAD
            ========================= */

            else {

                ctx.save();


                ctx.translate(x, y);


                let angle = 0;


                if (direction.x === -1) {

                    angle = Math.PI;

                }


                if (direction.y === -1) {

                    angle = -Math.PI / 2;

                }


                if (direction.y === 1) {

                    angle = Math.PI / 2;

                }


                ctx.rotate(angle);


                /*
                   Head shadow.
                */

                ctx.fillStyle =
                    "rgba(0,0,0,.12)";


                ctx.beginPath();

                ctx.ellipse(
                    1,
                    2,
                    11,
                    9,
                    0,
                    0,
                    Math.PI * 2
                );

                ctx.fill();


                /*
                   Head.
                */

                ctx.fillStyle =
                    snakeColor;


                ctx.beginPath();

                ctx.ellipse(
                    0,
                    0,
                    11,
                    9,
                    0,
                    0,
                    Math.PI * 2
                );

                ctx.fill();


                /* =========================
                   EYES
                ========================= */

                ctx.fillStyle = "white";


                ctx.beginPath();

                ctx.arc(
                    5,
                    -4,
                    3,
                    0,
                    Math.PI * 2
                );

                ctx.arc(
                    5,
                    4,
                    3,
                    0,
                    Math.PI * 2
                );

                ctx.fill();


                /* =========================
                   PUPILS
                ========================= */

                ctx.fillStyle = "#111";


                ctx.beginPath();

                ctx.arc(
                    6,
                    -4,
                    1.5,
                    0,
                    Math.PI * 2
                );

                ctx.arc(
                    6,
                    4,
                    1.5,
                    0,
                    Math.PI * 2
                );

                ctx.fill();


                /* =========================
                   TONGUE
                ========================= */

                ctx.strokeStyle = "#e53935";

                ctx.lineWidth = 1.5;


                ctx.beginPath();

                ctx.moveTo(10, 0);

                ctx.lineTo(16, 0);

                ctx.moveTo(16, 0);

                ctx.lineTo(19, -2);

                ctx.moveTo(16, 0);

                ctx.lineTo(19, 2);

                ctx.stroke();


                ctx.restore();

            }

        }

    );

}


/* =========================
   DRAW GAME
========================= */

function draw() {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    /*
       Draw the grid first
       so everything sits inside
       the cells.
    */

    drawGrid();


    /* =========================
       FOOD
    ========================= */

    ctx.font = "18px Arial";

    ctx.textAlign = "center";

    ctx.textBaseline = "middle";


    ctx.fillText(

        foodEmoji,

        food.x * cell + 10,

        food.y * cell + 10

    );


    /* =========================
       SNAKE
    ========================= */

    drawSnake();


    /* =========================
       GAME OVER
    ========================= */

    if (gameOver) {

        /*
           Dark transparent overlay.
        */

        ctx.fillStyle =
            "rgba(255,255,255,.84)";


        ctx.fillRect(
            28,
            115,
            304,
            130
        );


        ctx.fillStyle =
            "#303640";


        ctx.font =
            "bold 29px Arial";


        ctx.fillText(
            "Game Over!",
            180,
            150
        );


        ctx.font =
            "16px Arial";


        ctx.fillText(
            "You hit the wall!",
            180,
            180
        );


        ctx.font =
            "bold 17px Arial";


        ctx.fillText(
            "🏆 Score: " + score,
            180,
            211
        );

    }

}


/* =========================
   ARROW CONTROLS
========================= */

function addControl(id, x, y) {

    document
        .getElementById(id)
        .addEventListener(

            "pointerdown",

            function(event) {

                event.preventDefault();

                changeDirection(x, y);

            }

        );

}


addControl("up", 0, -1);

addControl("down", 0, 1);

addControl("left", -1, 0);

addControl("right", 1, 0);


/* =========================
   SWIPE CONTROLS
========================= */

let touchStartX = 0;

let touchStartY = 0;


canvas.addEventListener(

    "touchstart",

    function(event) {

        event.preventDefault();


        const touch =
            event.touches[0];


        touchStartX =
            touch.clientX;


        touchStartY =
            touch.clientY;

    },

    {passive: false}

);


canvas.addEventListener(

    "touchend",

    function(event) {

        event.preventDefault();


        const touch =
            event.changedTouches[0];


        const dx =
            touch.clientX - touchStartX;


        const dy =
            touch.clientY - touchStartY;


        const minSwipe = 25;


        if (

            Math.abs(dx) < minSwipe &&
            Math.abs(dy) < minSwipe

        ) {

            return;

        }


        if (

            Math.abs(dx) > Math.abs(dy)

        ) {

            if (dx > 0) {

                changeDirection(1, 0);

            }

            else {

                changeDirection(-1, 0);

            }

        }

        else {

            if (dy > 0) {

                changeDirection(0, 1);

            }

            else {

                changeDirection(0, -1);

            }

        }

    },

    {passive: false}

);


/* =========================
   KEYBOARD
========================= */

document.addEventListener(

    "keydown",

    function(event) {

        const key =
            event.key.toLowerCase();


        if (

            event.key === "ArrowUp" ||
            key === "w"

        ) {

            event.preventDefault();

            changeDirection(0, -1);

        }


        if (

            event.key === "ArrowDown" ||
            key === "s"

        ) {

            event.preventDefault();

            changeDirection(0, 1);

        }


        if (

            event.key === "ArrowLeft" ||
            key === "a"

        ) {

            event.preventDefault();

            changeDirection(-1, 0);

        }


        if (

            event.key === "ArrowRight" ||
            key === "d"

        ) {

            event.preventDefault();

            changeDirection(1, 0);

        }

    }

);


/* =========================
   CUSTOMIZE PANEL
========================= */

document
    .getElementById("customize")
    .addEventListener(

        "click",

        function() {

            document
                .getElementById("customPanel")
                .classList.toggle("open");

        }

    );


/* =========================
   SNAKE COLORS
========================= */

document
    .querySelectorAll(
        ".choice:not(.food)"
    )
    .forEach(

        function(button) {

            button.addEventListener(

                "click",

                function() {

                    document
                        .querySelectorAll(
                            ".choice:not(.food)"
                        )
                        .forEach(

                            function(b) {

                                b.classList.remove(
                                    "selected"
                                );

                            }

                        );


                    button.classList.add(
                        "selected"
                    );


                    snakeColor =
                        button.dataset.color;


                    draw();

                }

            );

        }

    );


/* =========================
   FOOD
========================= */

document
    .querySelectorAll(".food")
    .forEach(

        function(button) {

            button.addEventListener(

                "click",

                function() {

                    document
                        .querySelectorAll(
                            ".food"
                        )
                        .forEach(

                            function(b) {

                                b.classList.remove(
                                    "selected"
                                );

                            }

                        );


                    button.classList.add(
                        "selected"
                    );


                    foodEmoji =
                        button.dataset.food;


                    draw();

                }

            );

        }

    );


/* =========================
   RESTART BUTTONS
========================= */

document
    .getElementById("restart")
    .addEventListener(
        "click",
        restart
    );


document
    .getElementById("gameOverRestart")
    .addEventListener(
        "click",
        restart
    );


/* =========================
   START GAME
========================= */

restart();

</script>

</body>
</html>
""", height=850)
