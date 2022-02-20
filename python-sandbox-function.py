def handler(request):
    class Business:
    
        def __init__(self, init_cost, rate_growth):
            self.init_cost = init_cost
            self.rate_growth = rate_growth

    lemonade_stand = Business(3.78,1.07)
    newspaper_delivery = Business(60,1.15)
    car_wash = Business(720,1.14)
    pizza_delivery = Business(8640,1.13)
    donut_shop = Business(103680,1.12)
    shrimp_boat = Business(1244160,1.11)
    hockey_team = Business(14929920,1.1)
    movie_studio = Business(179159040,1.09)
    bank = Business(2149908480,1.08)
    oil_company = Business(25798901760,1.07)

    print(lemonade_stand.init_cost)
    print(newspaper_delivery.init_cost)
    print(car_wash.init_cost)
    print(pizza_delivery.init_cost)
    print(donut_shop.init_cost)
    print(shrimp_boat.init_cost)
    print(hockey_team.init_cost)
    print(movie_studio.init_cost)
    print(bank.init_cost)
    print(oil_company.init_cost)    
    return "Successfully executed"
