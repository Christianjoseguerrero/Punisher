from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_CASTIGADOR = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dossier Clasificado - Punisher</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Courier New', Courier, monospace; }
        body { background-color: #050505; color: #e0e0e0; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; overflow-x: hidden; }
        body::before { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: linear-gradient(rgba(153, 27, 27, 0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(153, 27, 27, 0.04) 1px, transparent 1px); background-size: 20px 20px; z-index: 0; pointer-events: none; }
        .contenedor-tactico { width: 100%; max-width: 450px; background-color: #0d0d0d; border: 2px solid #991b1b; border-radius: 4px; padding: 30px; text-align: center; box-shadow: 0 0 25px rgba(153, 27, 27, 0.3); position: relative; z-index: 1; }
        .header-dossier { border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 25px; text-align: left; font-size: 0.8rem; color: #777; text-transform: uppercase; letter-spacing: 2px; }
        .header-dossier span { color: #991b1b; font-weight: bold; }
        .skull-container { margin: 20px auto; width: 120px; height: 150px; }
        .skull-svg { width: 100%; height: 100%; fill: #e0e0e0; filter: drop-shadow(0 0 10px rgba(153, 27, 27, 0.6)); }
        h1 { color: #ffffff; font-size: 1.8rem; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 5px; }
        .subtitulo { color: #991b1b; font-size: 0.95rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
        .pregunta-central { background-color: #141414; border-left: 4px solid #991b1b; padding: 15px; margin-bottom: 35px; font-size: 1.1rem; text-align: left; line-height: 1.4; color: #ffffff; text-transform: uppercase; }
        .opciones-container { display: flex; gap: 20px; justify-content: center; }
        .btn-militar { flex: 1; padding: 15px; font-size: 1.2rem; font-weight: bold; text-transform: uppercase; cursor: pointer; border: 1px solid #333; background-color: #111; color: #b3b3b3; transition: all 0.2s ease; }
        .btn-si { border-color: #991b1b; color: #ffffff; background: linear-gradient(135deg, #4c0519, #991b1b); box-shadow: 0 4px 10px rgba(153, 27, 27, 0.2); }
        .btn-si:hover { background: linear-gradient(135deg, #991b1b, #b91c1c); box-shadow: 0 0 15px #ff0000; }
        .btn-no { border-color: #333; background-color: #161616; }
        .btn-no:hover { background-color: #262626; color: #ffffff; }
        .pie-codigo { margin-top: 35px; font-size: 0.7rem; color: #444; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="contenedor-tactico">
        <div class="header-dossier">ID-SISTEMA: <span>PUNISHER-01</span><br>ESTADO: OPERATIVO EN TIEMPO REAL</div>
        <h1>puesme & Cristian</h1>
        <div class="subtitulo">Un Amor de Punisher</div>
        <div class="skull-container">
            <svg class="skull-svg" viewBox="0 0 100 130">
                <path d="M 50,5 C 25,5 15,20 15,45 C 15,55 18,65 22,70 C 25,65 30,60 38,62 C 45,64 48,58 50,58 C 52,58 55,64 62,62 C 70,60 75,65 78,70 C 82,65 85,55 85,45 C 85,20 75,5 50,5 Z"/>
                <path d="M 23,73 L 26,115 L 34,115 L 35,82 L 42,82 L 43,125 L 50,125 L 50,82 L 50,125 L 57,125 L 58,82 L 65,82 L 66,115 L 74,115 L 77,73 C 71,78 64,74 58,76 C 55,77 52,74 50,74 C 48,74 45,77 42,76 C 36,74 29,78 23,73 Z"/>
                <path d="M 28,38 C 34,35 41,40 43,45 C 38,46 32,44 28,38 Z" fill="#050505"/>
                <path d="M 72,38 C 66,35 59,40 57,45 C 62,46 68,44 72,38 Z" fill="#050505"/>
                <path d="M 50,48 L 46,56 L 50,54 L 54,56 Z" fill="#050505"/>
            </svg>
        </div>
        <div class="pregunta-central">¿Pasar toda la vida con tu punisher?</div>
        <form action="/responder" method="POST">
            <div class="opciones-container">
                <button type="submit" name="voto" value="SI" class="btn-militar btn-si">SÍ</button>
                <button type="submit" name="voto" value="NO" class="btn-militar btn-no">NO</button>
            </div>
        </form>
        <div class="pie-codigo">SISTEMA ENCRIPTADO // REGISTRO DIRECTO</div>
    </div>
</body>
</html>
"""

@app.route('/')
def inicio():
    return render_template_string(HTML_CASTIGADOR)

@app.route('/responder', methods=['POST'])
def responder():
    voto = request.form.get('voto')
    # Imprime la respuesta en la consola del servidor web para verla en vivo
    print(f"[DECISIÓN TÁCTICA] Respuesta de puesme: {voto}", flush=True)
    return """
    <body style="background-color:#050505; color:#fff; font-family:monospace; display:flex; justify-content:center; align-items:center; height:100vh; margin:0; text-align:center;">
        <div style="border:1px solid #991b1b; padding:30px; box-shadow:0 0 15px #991b1b;">
            <h2 style="color:#991b1b; text-transform:uppercase; letter-spacing:2px;">Misión Procesada</h2>
            <p style="color:#888; margin-top:10px;">La respuesta ha sido enviada al centro de control.</p>
        </div>
    </body>
    """

# Variable requerida por servidores en la nube
app = app
