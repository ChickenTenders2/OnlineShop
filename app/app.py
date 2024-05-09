from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from ListItems import db, Sneaker
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask import jsonify

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite3"
app.config['SECRET_KEY'] = "the CSRF is protected by this password"
app.jinja_env.globals.update(zip=zip)
db.init_app(app)

class QuantityForm(FlaskForm):
    sneakerID = IntegerField(render_kw={'type': 'hidden'}, name='sneakerID')
    quantity = IntegerField('Quantity: ', validators = [DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Add to Basket')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = QuantityForm()
    sort_by = request.args.get('sort_by', 'price_asc') 
    if sort_by == 'price_asc':
        sneakers = Sneaker.query.order_by(Sneaker.price.asc()).all()  
    elif sort_by == 'price_desc':
        sneakers = Sneaker.query.order_by(Sneaker.price.desc()).all() 
    else:
        sneakers = Sneaker.query.all() 

    if form.validate_on_submit():
        sneakerID = form.sneakerID.data 
        if 'basket' not in session:
            session['basket'] = []
        if sneakerID:
            session['basket'].append({'item_id': int(sneakerID), 'quantity': form.quantity.data})
            session.modified = True
            flash('Item has been added to the basket.')
        else:
            flash('No sneaker ID provided')
            return redirect(url_for('home'))
    return render_template('index.html', sneakers=sneakers, form=form)

@app.route('/sneaker/<int:sneakerID>', methods=['GET', 'POST'])
def singleProductPage(sneakerID):
    form = QuantityForm()
    sneaker = Sneaker.query.get(sneakerID)
    if form.validate_on_submit():
        if 'basket' not in session:
            session['basket'] = []
        if sneakerID:
            session['basket'].append({'item_id': int(sneakerID), 'quantity': form.quantity.data})
            session.modified = True
            flash('Item has been added to the basket.')
        else:
            flash('No sneaker ID provided')
            return redirect(url_for('home'))
    return render_template('SingleSneaker.html', sneaker=sneaker, form = form)

@app.route('/basket')
def basket():
    basket = session.get('basket', [])
    items = [{'sneaker': Sneaker.query.get(item['item_id']), 'quantity': item['quantity']} for item in basket]
    total = 0
    for item in items:
        try:
            price = int(item['sneaker'].price.replace('£', ''))
            quantity = int(item['quantity'])
            total += price * quantity
        except ValueError:
            pass 
    return render_template('basket.html', items=items, total=total, checkout_url=url_for('checkout'))

def validate_payment(card_number, cvv, cardholder_name):
    if card_number and cvv and cardholder_name:
        return True
    else:
        return False

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        card_number = request.form.get('card-number')
        cvv = request.form.get('cvv')
        cardholder_name = request.form.get('cardholder-name')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        postcode = request.form.get('postcode')

        address = f"{address1}, {address2}, {city}, {postcode}"
        address = address or 'Default Address' 

        if validate_payment(card_number, cvv, cardholder_name):
            clear_basket()
            return redirect(url_for('success', address=address))
        else:
            flash('Payment failed. Please check your details and try again.')
    return render_template('checkout.html')

def clear_basket():
    session['basket'] = []

@app.route('/success')
def success():
    address = request.args.get('address', '')
    return render_template('PaymentSuccess.html', address=address)

@app.route('/delete_from_basket/<int:sneakerID>', methods=['POST'])
def delete_from_basket(sneakerID):
    basket = session.get('basket', [])
    for item in basket:
        if item['item_id'] == sneakerID:
            basket.remove(item)
            session['basket'] = basket
            session.modified = True
            flash('Item has been removed from the basket.')
            break
    return redirect(url_for('basket'))

@app.route('/sneaker-description/<int:sneakerID>')
def sneaker_description(sneakerID):
    sneaker = db.session.get(Sneaker, sneakerID)
    if sneaker is None:
        return jsonify(error='No sneaker found with this ID'), 404
    else:
        return jsonify(description=sneaker.description)
    
def perform_search(query):
    results = Sneaker.query.filter(Sneaker.name.ilike(f'%{query}%')).all()
    return results

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = perform_search(query)
    return render_template('search_results.html', results=results)
    
if __name__ == '__main__':
    app.run(debug=True)