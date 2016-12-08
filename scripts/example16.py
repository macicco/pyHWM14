
if __name__ == '__main__':

    def example16():

        from pyhwm2014.pyhwm14 import HWM142D, HWM142DPlot

        # Latitude vs Longitude array
        hwm14Obj = HWM142D(alt=130., ap=[-1, 35], glatlim=[-90., 90.], glatstp=1., 
            glonlim=[-180., 180.], glonstp=2., option=6, verbose=False)

        # Latitude vs Longitude plot
        hwm14Gbj = HWM142DPlot( profObj=hwm14Obj, zMin=[-150., -150], zMax=[150., 150.] )

    example16()
