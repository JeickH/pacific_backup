from flask import Flask, request, make_response, redirect, render_template, Blueprint, current_app, send_from_directory
from blueprints.logo import logo_bp
import json
import os

app = Flask(__name__)

app.debug = True
app.register_blueprint(logo_bp)

"""
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)
"""

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/home'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/robots.txt')
def robots():
    robots_txt = "User-agent: *\nDisallow: /private\n"
    response = make_response(robots_txt)
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route('/home')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        #'todos': todos,
    }
    return render_template('index.html', **context)

@app.route("/buy")
def buy_tickets():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        #'todos': todos,
    }
    print(f'Compra iniciada')
    return render_template('buy.html', **context)


@app.route('/infraestructura')
def infraestructura():
    return render_template('infraestructura.html')

@app.route('/construccion')
def construccion():
    return render_template('construccion.html')

@app.route('/consultoria')
def consultoria():
    return render_template('consultoria.html')

@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/nosotros')
def nosotros():
    return render_template('quienes.html')

@app.route('/inspeccion_ditribucion')
def inspeccion_ditribucion():
    return render_template('inspeccion_acu/distribucion.html')

@app.route('/inspeccion_principales')
def inspeccion_principales():
    return render_template('inspeccion_acu/principales.html')

@app.route('/inspeccion_qv')
def inspeccion_qv():
    return render_template('inspeccion_tub/qv.html')

@app.route('/inspeccion_qv360')
def inspeccion_qv360():
    return render_template('inspeccion_tub/qvtressesenta.html')

@app.route('/inspeccion_rx')
def inspeccion_rx():
    return render_template('inspeccion_tub/rx.html')

@app.route('/inspeccion_vsultra')
def inspeccion_vsultra():
    return render_template('inspeccion_tub/vsultra.html')

@app.route('/limpieza_general')
def limpieza_general():
    return render_template('limpieza/general.html')

@app.route('/limpieza_rom')
def limpieza_rom():
    return render_template('limpieza/rom.html')

@app.route('/limpieza_s')
def limpieza_s():
    return render_template('limpieza/s-products.html')

@app.route('/rehabilitacion_equipos')
def rehabilitacion_equipos():
    return render_template('rehabilitacion/equipos.html')

@app.route('/rehabilitacion_materiales')
def rehabilitacion_materiales():
    return render_template('rehabilitacion/materiales.html')

@app.route('/servicios_diseno')
def servicios_diseno():
    return render_template('servicios/diseno.html')

@app.route('/servicios_equipos')
def servicios_equipos():
    return render_template('servicios/equipos.html')

@app.route('/servicios_fugas')
def servicios_fugas():
    return render_template('servicios/fugas.html')

@app.route('/servicios_inspeccion')
def servicios_inspeccion():
    return render_template('servicios/inspeccion.html')

@app.route('/servicios_limpieza')
def servicios_limpieza():
    return render_template('servicios/limpieza_redes.html')

@app.route('/servicios_mapeo')
def servicios_mapeo():
    return render_template('servicios/mapeo.html')

@app.route('/servicios_rehabilitacion')
def servicios_rehabilitacion():
    return render_template('servicios/rehabilitacion_redes.html')

@app.route('/soporte_limpieza')
def soporte_limpieza():
    return render_template('soporte/limpieza.html')

@app.route('/soporte_robotizados')
def soporte_robotizados():
    return render_template('soporte/robotizados.html')

@app.route('/wincan')
def wincan():
    return render_template('wincan.html')

@app.route('/griferia')
def griferia():
    return render_template('productos/griferia.html')

@app.route('/accesorios')
def accesorios():
    return render_template('productos/bano.html')

@app.route('/duchas')
def duchas():
    return render_template('productos/duchas.html')

@app.route('/lavamanos')
def lavamanos():
    return render_template('productos/lavamanos.html')

@app.route('/sanitarios')
def sanitarios():
    return render_template('productos/sanitarios.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)