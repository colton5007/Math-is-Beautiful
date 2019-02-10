I once was told that the more confusing math becomes, the more elegant it is to the understood eye. It might
seem like chaos and magic to one person, but to a well trained mind and eye, it becomes an intricate series of
patterns. This is a playful utility that lets you experience the patterns for yourself. There is no graph, no
strict equations, no scary derivatives, or weird set theory, just a canvas and a few inputs where you can put
whatever your heart and mind desires (within reason). Simply give it an equation for R, G, B with parameters of
x and y, and see what gets draw onto the canvas in front of you. It might take a minute or two since this is
quite a sizable number of calculations, but it'll come to fruition. <br>

If you are interested in the calculations being done or the text parsing that takes place to allow
you to have such a pleasant environment to enter data in, please checkout the
<a href="https://github.com/colton5007/Math-is-Beautiful">github repo</a>. It might just seem like a pretty
image generator but there is a lot going on here. Over 3145728 calculations are done alone which is the shortest
part when you consider the effort it takes to parse even simple symbolic expressions and interpret them
programmatically.<br>

Whenever you are ready to try it out for yourself click the button below and I hope you have fun and
learn something.

If you want to try and spin this up for yourself, I regret to inform you it is a slight pain in the rear.
I apologize for the inconvenience associated with it but some of the libraries
I rely on are still in the python2 days. You'll need to install flask, sympy, pillow, numpy, and antlr4... all python2.
These grave costs are not without great reward; after the dreadful python2 is dusted off, to try it yourself is fairly 
straightforward. Simply spin it up with flask normally, or put it on heroku somewhere and call it a day. After that 
it'll just work and you'll be able to create your images and the serentity that comes with it.<br>

I will throw this up somewhere myself when I get the chance and update this repo accordingly.