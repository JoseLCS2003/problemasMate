from sympy import diff, symbols, sympify, lambdify

class MetodosMate:
    @staticmethod
    def euler_mejorado(x0, y0, h, xf, fxy):
        f = lambdify(['x', 'y'], sympify(fxy)) 
        xn = x0
        yn = y0
        resultado = []

        while xn < xf:
            yn1_est = yn + h * f(xn, yn) 
            xn1 = xn + h
            yn1 = yn + (h / 2) * (f(xn, yn) + f(xn1, yn1_est)) 
        
            resultado.append({
                "n": len(resultado),
                "Xn": xn,
                "Yn": yn,
                "(Yn+1)*": yn1_est,
                "Xn+1": xn1,
                "Yn+1": yn1
            })

            xn = xn1
            yn = yn1

        return resultado
    
    @staticmethod
    def runge_kutta(x0,y0,h,xf,fxy):
        f = lambdify(['x', 'y'], sympify(fxy))
        xn=x0
        yn=y0
        resultado =[]

        while xn < xf:
            k1=f(xn,yn)
            k2=f(xn+h/2,yn+(h*k1)/2)
            k3=f(xn+h/2,yn+(h*k2)/2)
            k4=f(xn+h,yn+h*k3)

            yn1= yn+(h/6)*(k1+2*k2+2*k3+k4)
            xn1=xn+h
            resultado.append({
                "n":len(resultado),
                "Xn":xn,
                "Yn":yn,
                "K1":k1,
                "K2":k2,
                "K3":k3,
                "K4":k4,
                "Yn+1":yn1
            })
            xn=xn1
            yn=yn1

        return resultado

    @staticmethod
    def newthon_raphson(x1, fx, precision):
        x = symbols('x')
        f_expr = fx
        f_prime_expr = diff(f_expr, x)

        f = lambdify(x, f_expr)
        f_prime = lambdify(x, f_prime_expr)

        x_n = x1
        resultado = []

        while True:
            f_xn = f(x_n)
            f_prime_xn = f_prime(x_n)

            if f_prime_xn == 0:
                return resultado  # Evitar división por cero

            x_next = x_n - f_xn / f_prime_xn

            resultado.append({
                "n": len(resultado),
                "Xn": round(x_n, precision),
                "Xn+1": round(x_next, precision)
            })

            # Condición de parada basada en la precisión
            if abs(x_next - x_n) < 10**(-precision):
                return resultado

            x_n = x_next

            