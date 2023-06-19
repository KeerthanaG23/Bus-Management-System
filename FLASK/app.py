from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adding', methods=['GET', 'POST'])
def adding():

    val1 = request.form.get('START')
    val2 = request.form.get('DEST')
    strnew = []
    strnew = calc(val1, val2)
    return render_template("index.html", dist=strnew[0], route=strnew[1])


def calc(val1, val2):
    import csv
    print("================================================================================================================")
    print("")
    print("\t\t\t\tWELCOME TO MTC BUS ROUTE MANAGEMENT")
    print("")
    print("================================================================================================================")
    print("")
    print("")
    source = val1
    print("")
    print("")
    destination = val2
    print("")
    print("")
    file = open("raw.csv", "r")
    reader = csv.reader(file)

    route_num = []
    route_stops = []
    for row in reader:
        if row != []:
            route_num.append(row[0])
            route_stops.append(row[1])
    brd = dict(zip(route_num, route_stops))
    del brd['']

    count = 0
    min = 99999999999999999999999
    for brn in brd:
        bus_route = brd[brn]
        if ((source in bus_route) and (destination in bus_route)):
            count += 1
            src_ind = bus_route.index(source)
            dest_ind = bus_route.index(destination)
            cost = dest_ind - src_ind - 1
            if (cost < 0):
                cost = -1*cost
            if (cost <= min):
                min = cost
                min_route = brn

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print("\t\t\t\tSHORTEST BUS ROUTE : ")
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    if (count != 0):
        # print("\tBUS NUMBER : ",min_route)
        # print("\tSTOP LIST : ",brd[min_route])
        ar = [min_route, brd[min_route]]
        return (ar)
    else:
        str = "ROUTE UNAVAILABLE"
        return str
        # print("\tROUTE UNAVAILABLE")
    print("")
    print("")
    print("================================================================================================================")
    print("")
    print("\t\t\t\tEND OF PAGE")
    print("")
    print("================================================================================================================")


if __name__ == "__main__":
    app.run()
