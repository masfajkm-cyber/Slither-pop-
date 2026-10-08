import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SlitherPop",
    page_icon="🐍"
)

st.markdown("""
<h1 style="text-align:center;">SlitherPop</h1>
<p style="text-align:center;">by Masfa</p>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: #f8c8dc;
    font-family: Arial, sans-serif;
    text-align: center;
}

h2 {
    color: #b1124a;
}

#score {
    color: #b1124a;
    font-size: 22px;
    font-weight: bold;
}

canvas {
    background: #fff0f6;
    border: 5px solid #b1124a;
    border-radius: 20px;
    max-width: 90vw;
}

button {
    background: #f4a9c4;
    color: #b1124a;
    border: none;
    border-radius: 12px;
    padding: 10px 18px;
    margin: 5px;
    font-size: 18px;
    font-weight: bold;
}
</style>
</head>

<body>

<h2>🐍 SlitherPop</h2>
<div id="score">Score: 0</div>

<canvas id="game" width="360" height="360"></canvas>

<br>

<button onclick="restart()">🔄 Restart</button>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let snake;
let food;
let direction;
let score;
let gameOver;

function restart() {
    snake = [
        {x: 180, y: 180},
        {x: 160, y: 180},
        {x: 140, y: 180}
    ];

    direction = {x: 20, y: 0};
    score = 0;
    gameOver = false;

    createFood();
}

function createFood() {
    food = {
        x: Math.floor(Math.random() * 18) * 20,
        y: Math.floor(Math.random() * 18) * 20
    };
}

function draw() {

    if (gameOver) {
        ctx.fillStyle = "#b1124a";
        ctx.font = "bold 30px Arial";
        ctx.textAlign = "center";
        ctx.fillText("Game Over!", 180, 170);

        ctx.font = "20px Arial";
        ctx.fillText("Press Restart", 180, 205);
        return;
    }

    ctx.clearRect(0, 0, 360, 360);

    // Food
    ctx.fillStyle = "#b1124a";
    ctx.beginPath();
    ctx.arc(food.x + 10, food.y + 10, 8, 0, Math.PI * 2);
    ctx.fill();

    // Snake
    snake.forEach((part, index) => {
        ctx.fillStyle = index === 0 ? "#8f0d3b" : "#d94f7d";
        ctx.fillRect(part.x + 1, part.y + 1, 18, 18);
    });

    let head = {
        x: snake[0].x + direction.x,
        y: snake[0].y + direction.y
    };

    // Wall collision
    if (
        head.x < 0 ||
        head.x >= 360 ||
        head.y < 0 ||
        head.y >= 360
    ) {
        gameOver = true;
        return;
    }

    // Body collision
    for (let part of snake) {
        if (head.x === part.x && head.y === part.y) {
            gameOver = true;
            return;
        }
    }

    snake.unshift(head);

    // Food collision
    if (head.x === food.x && head.y === food.y) {
        score++;
        document.getElementById("score").innerText =
            "Score: " + score;
        createFood();
    } else {
        snake.pop();
    }
}

document.addEventListener("keydown", function(event) {

    if (event.key === "ArrowUp" && direction.y === 0)
        direction = {x: 0, y: -20};

    if (event.key === "ArrowDown" && direction.y === 0)
        direction = {x: 0, y: 20};

    if (event.key === "ArrowLeft" && direction.x === 0)
        direction = {x: -20, y: 0};

    if (event.key === "ArrowRight" && direction.x === 0)
        direction = {x: 20, y: 0};
});

restart();

setInterval(draw, 120);

</script>

</body>
</html>
""", height=500)
