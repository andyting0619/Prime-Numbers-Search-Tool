from prime_number import search_prime
from flask import Flask, render_template, request, redirect
import html


app = Flask(__name__)


@app.route('/search', methods=['POST'])
def do_search() -> html:
    lower_bound = request.form['lower bound']
    upper_bound = request.form['upper bound']
    title = 'Prime numbers search result:'
    title2 = 'Prime number testing result:'
    output = search_prime(int(lower_bound), int(upper_bound))
    results = str(output)
    if int(lower_bound) > int(upper_bound):
        return redirect('/error')
    elif int(lower_bound) < 2 and int(upper_bound) > 1:
        return redirect('/error2')
    elif int(upper_bound) < 2:
        return redirect('/error3')
    elif int(lower_bound) < int(upper_bound) and len(output) > 1:
        return render_template('results.html', the_lower_bound=lower_bound, the_upper_bound=upper_bound, the_title=title, number_of_primes=str(len(output)), the_results=results)
    elif int(lower_bound) < int(upper_bound) and len(output) == 1:
        return render_template('results2.html', the_lower_bound=lower_bound, the_upper_bound=upper_bound, the_title=title, the_results=str(output[0]))
    elif int(lower_bound) < int(upper_bound) and len(output) == 0:
        return render_template('results3.html', the_lower_bound=lower_bound, the_upper_bound=upper_bound, the_title=title)
    elif int(lower_bound) == int(upper_bound):
        if len(output) == 1:
            return render_template('results4.html', the_title=title2, the_results=str(lower_bound))
        elif len(output) == 0:
            return render_template('results5.html', the_title=title2, the_results=str(lower_bound))


@ app.route('/')
@ app.route('/entry')
def entry_page() -> html:
    return render_template('entry.html', the_title='Welcome to prime numbers search tool on the web!')


@ app.route('/error')
def error_page() -> html:
    return render_template('error.html', the_title='The upper bound cannot be smaller than the lower bound!')


@app.route('/error2')
def error2_page() -> html:
    return render_template('error2.html', the_title='The lower bound cannot be smaller than 2!')


@app.route('/error3')
def error3_page() -> html:
    return render_template('error3.html', the_title='Both the lower and upper bounds cannot be smaller than 2!')


if __name__ == '__main__':
    app.run(debug=True)
