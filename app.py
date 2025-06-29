from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Halo Riskya!</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: white;
                padding: 2rem 3rem;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                text-align: center;
                animation: fadeIn 1s ease-in;
            }
            h1 {
                margin-bottom: 0.5rem;
            }
            p {
                font-size: 1.2rem;
            }
            .button {
                margin-top: 1.5rem;
                padding: 0.7rem 1.5rem;
                font-size: 1rem;
                color: white;
                background: linear-gradient(45deg, #007bff, #00d4ff);
                border: none;
                border-radius: 30px;
                cursor: pointer;
                transition: 0.3s;
            }
            .button:hover {
                transform: scale(1.05);
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Halo, Riskya Egi Pratama!</h1>
            <p>Selamat datang di Web Saya
            <p><strong>NIM:</strong> A710230031</p>
            <form action="/how-are-you">
                <button class="button" type="submit">Tanya Kabar</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/how-are-you")
def how_are_you():
    return """
    <h2>Saya baik, Riskya! 😊</h2>
    <p><a href="/">Kembali ke halaman utama</a></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
