
    d3.wordcloud()
        .size([800, 400])
        .selector('#wordcloud')
        //.words([{text: 'word', size: 5}, {text: 'cloud', size: 15}])
        .words([
            {text: '', size: 0}
            {% for word in words %}
            ,{text: {{ word[0] }}, size: {{ word[1] }}}
            {% endfor %}
        ])
        .start();

function update_values() {
    d3.wordcloud()
        .size([800, 400])
        .selector('#wordcloud')
        //.words([{text: 'word', size: 5}, {text: 'cloud', size: 15}])
        .words([
            {text: '', size: 0}
            {% for word in words %}
            ,{text: {{ word[0] }}, size: {{ word[1] }}}
            {% endfor %}
        ])
        .start();
}
