import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SlitherPop",
    page_icon="🐍"
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
    background: #ffffff;
    font-family: Arial, sans-serif;
    text-align: center;
    color: #b1124a;
}

.title {
    font-size: 38px;
    font-weight: 900;
    margin-top: 5px;
}

.by {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 12px;
}

.settings {
    background: #f8c8dc;
    border-radius: 20px;
    padding: 12px;
    max-width: 390px;
    margin: auto;
}

label {
    font-weight: bold;
    font-size: 16px;
}

select {
    border: none;
    border-radius: 10px;
    padding: 8px;
    margin: 5px;
    font-size: 16px;
    background: white;
}

.score {
    font-size: 21px;
    font-weight: bold;
    margin: 10px;
}

canvas {
    width: min(90vw, 360px);
    height: min(90vw, 360px);
    background: #fff1f7;
    border: 5px solid #b1124a;
    border-radius: 22px;
    display: block;
    margin: auto;
}

.controls {
    width: 220px;
    margin: 12px auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}

.control {
    height: 55px;
    border: none;
    border-radius: 15px;
    background: #f4a9c4;
    color: #b1124a;
    font-size: 25px;
    font-weight: bold;
    touch-action: manipulation;
}

.control:active {
    background: #e88aaa;
    transform: scale(0.95);
}

.empty {
    visibility: hidden;
}

.restart {
    border: none;
    border-radius: 14px;
    background: #b1124a;
    color: white;
    padding: 11px 25px;
    font-size: 17px;
    font-weight: bold;
    margin-bottom: 15px;
}

</style>

</head>

<body>

<div class="title">SlitherPop</div>
<div class="by">by Masfa</div>

<div class="settings">

    <label>🐍 Snake Color</label>
    <br>

    <select id="snakeColor">
        <option value="#d94f7d">Pink</option>
        <option value="#e53935">Red</option>
        <option value="#2196f3">Blue</option>
        <option value="#4caf50">Green</option>
        <option value="#9c27b0">Purple</option>
        <option value="#111111">Black</option>
        <option value="#ff9800">Orange</option>
    </select>

    <br>

    <label>🍎 Food</label>
    <br>

    <select id="foodChoice">
        <option value="🍎">Apple</option>
        <option value="🍓">Strawberry</option>
        <option value="🍒">Cherries</option>
        <option value="🍇">Grapes</option>
        <option value="🍊">Orange</option>
        <option value="🍉">Watermelon</option>
        <option value="🍕">Pizza</option>
        <option value="🍩">Donut</option>
    </select>

</div>

<div class="score" id="score">
    Score: 0
</div>

<canvas id="game" width="360" height="360"></canvas>

<div class="controls">

    <div class="empty"></div>

    <button class="control" id="up">⬆️</button>

    <div class="empty"></div>

    <button class="control" id="left">⬅️</button>

    <button class="control" id="down">⬇️</button>

    <button class="control" id="right">➡️</button>

</div>

<button class="restart" id="restart">
    🔄 Restart
</button>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const grid = 18;
const cell = 20;

let snake;
let direction;
let nextDirection;
let food;
let score;
let gameOver = false;

const snakeColor = document.getElementById("snakeColor");
const foodChoice = document.getElementById("foodChoice");
const scoreDisplay = document.getElementById("score");

function restart() {

    snake = [
        {x: 9, y: 9},
        {x: 8, y: 9},
        {x: 7, y: 9}
    ];

    direction = {x: 1, y: 0};
    nextDirection = {x: 1, y: 0};

    score = 0;
    gameOver = false;

    scoreDisplay.textContent = "Score: 0";

    createFood();
}

function createFood() {

    food = {
        x: Math.floor(Math.random() * grid),
        y: Math.floor(Math.random() * grid)
    };

}

function changeDirection(x, y) {

    nextDirection = {
        x: x,
        y: y
    };

}

function moveSnake() {

    if (gameOver) {
        return;
    }

    direction = nextDirection;

    const head = {
        x: snake[0].x + direction.x,
        y: snake[0].y + direction.y
    };

    // ONLY WALL COLLISION MATTERS
    if (
        head.x < 0 ||
        head.x >= grid ||
        head.y < 0 ||
        head.y >= grid
    ) {

        gameOver = true;
        return;

    }

    snake.unshift(head);

    if (
        head.x === food.x &&
        head.y === food.y
    ) {

        score++;

        scoreDisplay.textContent =
            "Score: " + score;

        createFood();

    } else {

        snake.pop();

    }

}

function draw() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Food
    ctx.font = "18px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    ctx.fillText(
        foodChoice.value,
        food.x * cell + 10,
        food.y * cell + 10
    );

    // Snake
    snake.forEach((part, index) => {

        const radius = index === 0 ? 9 : 7;

        ctx.fillStyle = snakeColor.value;

        ctx.beginPath();

        ctx.arc(
            part.x * cell + 10,
            part.y * cell + 10,
            radius,
            0,
            Math.PI * 2
        );

        ctx.fill();

    });

    if (gameOver) {

        ctx.fillStyle = "rgba(255,255,255,0.85)";
        ctx.fillRect(35, 135, 290, 90);

        ctx.fillStyle = "#b1124a";
        ctx.font = "bold 30px Arial";

        ctx.fillText(
            "Game Over!",
            180,
            170
        );

        ctx.font = "18px Arial";

        ctx.fillText(
            "You hit the wall!",
            180,
            200
        );

    }

}

function gameLoop() {

    moveSnake();
    draw();

}

function buttonControl(button, x, y) {

    button.addEventListener("pointerdown", function(event) {

        event.preventDefault();
        changeDirection(x, y);

    });

}

buttonControl(
    document.getElementById("up"),
    0,
    -1
);

buttonControl(
    document.getElementById("down"),
    0,
    1
);

buttonControl(
    document.getElementById("left"),
    -1,
    0
);

buttonControl(
    document.getElementById("right"),
    1,
    0
);

document.addEventListener("keydown", function(event) {

    if (event.key === "ArrowUp" || event.key === "w") {
        changeDirection(0, -1);
    }

    if (event.key === "ArrowDown" || event.key === "s") {
        changeDirection(0, 1);
    }

    if (event.key === "ArrowLeft" || event.key === "a") {
        changeDirection(-1, 0);
    }

    if (event.key === "ArrowRight" || event.key === "d") {
        changeDirection(1, 0);
    }

});

document.getElementById("restart")
    .addEventListener("click", restart);

snakeColor.addEventListener("change", draw);
foodChoice.addEventListener("change", draw);

restart();

setInterval(gameLoop, 110);

</script>

</body>
</html>
""", height=720)
