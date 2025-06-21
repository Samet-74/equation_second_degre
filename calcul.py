from math import sqrt

class Calcul:
    
    def recup_nb(self):
        print("Entrer la valeur de a s'il vous plaît")
        self.a = int(input())

        print("Entrer la valeur de b s'il vous plaît")
        self.b = int(input())

        print("Entrer la valeur de c s'il vous plaît")
        self.c = int(input())

        # return (self.a, self.b, self.c)


    def delta(self):
        self.delta = self.b**2 - (4*self.a*self.c)
        print(f"Le discriminant vaut: {self.delta}")
        if self.delta > 0:
            print("Le discriminant Δ est positif.")
        elif self.delta == 0:
            print("Le discriminant Δ est neutre.")
        else:
            print("Le discriminant Δ est négatif.")

    def determin_x(self):
        print("Maintenant cherchons les solutions")
        if self.delta > 0:
            self.x_reelle_1 = (-self.b + sqrt(self.delta))/(2*self.a)
            self.x_reelle_2 = (-self.b - sqrt(self.delta))/(2*self.a)
            print(f"Solutions: x1 = { self.x_reelle_1}, x2= { self.x_reelle_2}")
            return self.x_reelle_1, self.x_reelle_2
        elif self.delta == 0:
            self.x_double = (-self.b)/(2*self.a)
            print(f"La solution est {self.x_double}")
            return self.x_double
        else:
            self.result_delta_n = "Delta est négatif, ainsi il n'y a pas de racine "
            return self.result_delta_n
        
        
    
    def alpha_beta(self):
        print("Après avoir determiné les valeurs de x, il faut maintenant determiner alpha α et β pour pouvoir tracer le graphique.")
        self.alpha = (-self.b)/(2*self.a)
        self.beta = (self.a*self.alpha**2) + (self.b*self.alpha) + self.c
        print(f"Valeur d'alpha α: {self.alpha}  et valeur de beta β:    {self.beta}")
    
# a = Calcul()
# a.recup_nb()
# a.delta()
# # a.determin()
# a.alpha_beta()
