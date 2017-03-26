(function() {
    d3.wordcloud()
        .size([1200, 600])
        .selector('#wordcloud')
        .words([
            {% for word in words %}
            {text: '{{ word[0] }}', size: {{ word[1] }}},
            {% endfor %}
            {text: '', size: 0}
        ])
        .start();
}());
