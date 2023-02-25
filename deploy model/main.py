from flask import Flask,render_template,request
from sklearn.cluster import KMeans

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html',flash_message="False")

def get_labels(x,y,k):
  x1 = [int(i) for i in x.split(',')]
  y1 = [int(i) for i in y.split(',')]
  data = list(zip(x1, y1))
  kmeans = KMeans(n_clusters=int(k),n_init='auto')
  kmeans.fit(data)
  result = ''
  for i in kmeans.labels_:
    result = result + str(i) + ','
  return result

@app.route('/predict',methods=['POST'])
def predict():
  flag = False
  try:
    x = request.form.get('x')
    y = request.form.get('y')
    k = request.form.get('kval')
    chack = x.split(',')   
  except:
     flag = True

  if(flag or len(x)==0 or x==None or len(chack)<=2 and int(k)<len(chack)):
      return render_template('index.html',flash_message="False")
  else:
      result = get_labels(x,y,k)
      return render_template('index.html',flash_message="True",result=result,point_x = x,point_y = y)

if __name__ =='__main__':
  app.run(debug=True)