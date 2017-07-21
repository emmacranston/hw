import pandas as pd

def date_convert(string):
	s = string
	vals = s.split("/")
	if len(str(vals[2])) == 2:
		y = str(vals[2])
	else:
		y = "0" + str(vals[2])

	if len(str(vals[0])) == 2:
		m = str(vals[0])
	else: 
		m = "0" + str(vals[0])

	if len(str(vals[1])) == 2:
		d = str(vals[1])
	else:
		d = "0" + str(vals[1])

	return "20%s-%s-%s" % (y, m, d)

print date_convert("1/5/10")
print date_convert("12/12/12")
print date_convert("1/12/12")

orders = pd.read_csv("/Users/emmacranston/Documents/analyst_homework/orders.csv", sep=',', delimiter=None, header=0, index_col=0)
organizers = pd.read_csv("/Users/emmacranston/Documents/analyst_homework/organizers.csv", header=0, index_col=0)
events = pd.read_csv("/Users/emmacranston/Documents/analyst_homework/events.csv", header=0, index_col=0)

#convert dates in organizers table
organizers["signup_date"] = organizers["signup_date"].apply(lambda x : date_convert(x))
organizers["first_event_create_date"] = organizers["first_event_create_date"].apply(lambda x : date_convert(x))
organizers["first_publish_date"] = organizers["first_publish_date"].apply(lambda x : date_convert(x))

#lots of "NULL" in this .csv, so we convert them to strings so they don't confuse
organizers["first_paid_publish_date"] = organizers["first_paid_publish_date"].apply(lambda x: None if type(x) == float else date_convert(x))

#convert dates in events table
events["event_create_date"] = events["event_create_date"].apply(lambda x: None if type(x)!= str else date_convert(x))
events["event_publish_date"] = events["event_publish_date"].apply(lambda x: None if type(x)!= str else date_convert(x))
events["event_start_date"] = events["event_start_date"].apply(lambda x: None if type(x)!= str else date_convert(x))

#convert those obnoxious float values in orders
print orders.head(n=5)
orders["order_revenue"] = orders["order_revenue"].apply(lambda x: round(x,3))
print orders.head(n=5)
#now save the dataframes to another .csv filepath for upload to MySQL
events.to_csv("event.csv")
organizers.to_csv("organizer.csv")
orders.to_csv('order.csv')

