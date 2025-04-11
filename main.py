from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class ResultadoExamenCPUCursoRptaTO(ComplexModel):
    NNuPgta = Integer
    SCoRptaAlum = Unicode
    SCoRptaOK = Unicode


class VResultadoExamenCursoItem(ComplexModel):
    NCoCurs = Integer
    SNoCmpCurs = Unicode
    SNtEval = Unicode
    VResultadoExamenCPUCursoRptaTO = Array(ResultadoExamenCPUCursoRptaTO)


class ResultadoExamen(ComplexModel):
    NAaCicl = Integer
    NCoAlum = Integer
    NCoSecc = Integer
    NNuCicl = Integer
    SNoCmpPers = Unicode
    SNoCmpTest = Unicode
    VResultadoExamenCurso = Array(VResultadoExamenCursoItem)


class WMensajeInfoCPUItem(ComplexModel):
    coMsj = Unicode
    txMensaje = Unicode


class InfoCpuULimaMovilReturn(ComplexModel):
    NReload = Integer
    NSegRefresh = Integer
    SMensajeFinal = Unicode
    WMensajeInfoCPU = Array(WMensajeInfoCPUItem)
    ciclo = Integer
    coEstd = Integer
    fgEstd = Unicode
    resultadoExamen = ResultadoExamen


class InfoCpuULimaMovilResponse(ComplexModel):
    infoCpuULimaMovilReturn = InfoCpuULimaMovilReturn


class ULimaMovilService(ServiceBase):
    @rpc(_returns=InfoCpuULimaMovilResponse)
    def infoCpuULimaMovil(ctx):
        return InfoCpuULimaMovilResponse(
            infoCpuULimaMovilReturn=InfoCpuULimaMovilReturn(
                NReload=1,
                NSegRefresh=5,
                SMensajeFinal="""<![CDATA[<Mensaje><texto><table width="100%" bgcolor="#FF7902">[...]</table></texto></Mensaje>]]>""",
                WMensajeInfoCPU=[
                    WMensajeInfoCPUItem(
                        coMsj="CPU_EV28_2",
                        txMensaje="""<![CDATA[<Mensaje><texto><b>USTED RENDIRÁ EL EXAMEN 4 EN EL AULA N-107 CARPETA 18</b></texto></Mensaje>]]>"""
                    )
                ],
                ciclo=20250,
                coEstd=1,
                fgEstd=None,
                resultadoExamen=ResultadoExamen(
                    NAaCicl=0,
                    NCoAlum=10250350,
                    NCoSecc=119,
                    NNuCicl=2025,
                    SNoCmpPers="METZGER / CUADRAO / GRACE LIANA",
                    SNoCmpTest="EXAMEN 4",
                    VResultadoExamenCurso=[
    VResultadoExamenCursoItem(
        NCoCurs=96,
        SNoCmpCurs="LETRAS",
        SNtEval="07",
        VResultadoExamenCPUCursoRptaTO=[
            ResultadoExamenCPUCursoRptaTO(NNuPgta=21, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=22, SCoRptaAlum='D', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=23, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=24, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=25, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=26, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=27, SCoRptaAlum='A', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=28, SCoRptaAlum='', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=29, SCoRptaAlum='B', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=30, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=31, SCoRptaAlum='C', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=32, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=33, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=34, SCoRptaAlum='', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=35, SCoRptaAlum='D', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=36, SCoRptaAlum='D', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=37, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=38, SCoRptaAlum='B', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=39, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=40, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=21, SCoRptaAlum='C', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=22, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=23, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=24, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=25, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=26, SCoRptaAlum='B', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=27, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=28, SCoRptaAlum='A', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=29, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=30, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=31, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=32, SCoRptaAlum='B', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=33, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=34, SCoRptaAlum='', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=35, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=36, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=37, SCoRptaAlum='B', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=38, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=39, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=40, SCoRptaAlum='', SCoRptaOK='D')
        ]
    ),
    VResultadoExamenCursoItem(
        NCoCurs=95,
        SNoCmpCurs="CIENCIAS",
        SNtEval="06",
        VResultadoExamenCPUCursoRptaTO=[
            ResultadoExamenCPUCursoRptaTO(NNuPgta=1, SCoRptaAlum='B', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=2, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=3, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=4, SCoRptaAlum='A', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=5, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=6, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=7, SCoRptaAlum='A', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=8, SCoRptaAlum='B', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=9, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=10, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=11, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=12, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=13, SCoRptaAlum='A', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=14, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=15, SCoRptaAlum='C', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=16, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=17, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=18, SCoRptaAlum='B', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=19, SCoRptaAlum='D', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=20, SCoRptaAlum='C', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=1, SCoRptaAlum='B', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=2, SCoRptaAlum='D', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=3, SCoRptaAlum='B', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=4, SCoRptaAlum='C', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=5, SCoRptaAlum='C', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=6, SCoRptaAlum='A', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=7, SCoRptaAlum='B', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=8, SCoRptaAlum='', SCoRptaOK='C'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=9, SCoRptaAlum='A', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=10, SCoRptaAlum='A', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=11, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=12, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=13, SCoRptaAlum='', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=14, SCoRptaAlum='C', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=15, SCoRptaAlum='', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=16, SCoRptaAlum='', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=17, SCoRptaAlum='D', SCoRptaOK='D'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=18, SCoRptaAlum='A', SCoRptaOK='A'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=19, SCoRptaAlum='', SCoRptaOK='B'),
            ResultadoExamenCPUCursoRptaTO(NNuPgta=20, SCoRptaAlum='D', SCoRptaOK='D')
        ]
    )
]
                )
            )
        )


application = Application(
    [ULimaMovilService],
    tns='ULimaMovilServiceITLAB',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Servicio SOAP corriendo en http://0.0.0.0:8000")
    wsgi_app = WsgiApplication(application)
    servidor = make_server('0.0.0.0', 8000, wsgi_app)
    servidor.serve_forever()