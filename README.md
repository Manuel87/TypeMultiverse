Multiverse Type Design Space (parametrical) Interpolation Interface 
===========
This is a proposal extending the well known Noordzij Cube (with three dimensions) to an infinite number of dimensions, while still being able to handle it. :)

This visualisation shows an example with about 16 dimensions/axes 
![Multiverse Root-Method Interpolation Interface](Interpolation-Root-Method_Multiverse-Structure-Interface.png)

Each Point can represent either a:<br />
• Master (editable/already edited Instance, any other/extern compatible design …) <br />
• Instance (a possiblity represented by any point in the design-space multiverse ;)<br />
• Parameter/Effect/Filter/Algorithm (a designed and engineered formal modifcation, using data from the Masters/Instances + other (user) inputs. (e.g. Path-Offset,Slant, Cursivy, box-shadow, Tension, RMX-Tools, …)


The main Root-Point represents a user defined default setup, which can be either a Master or an Instance. All other Points in the system are reffering to the Root-Point. This not only makes it much easier to grasp, suddenly the actual calculations  e.g. for an interpolation are getting much easier. (ToDo: adding an calculation example)


The actual technique is irrelevant! It could be:<br />
• Standard linear vector calculation (Interpoaltion)<br />
(restrictions are made quite clear here: http://partners.adobe.com/public/developer/en/font/5091.Design_MM_Fonts.pdf (p.12-17) <br />
• Elaborated vector calculation (not seen yet ^^)<br />
• Kalliculator calculations <br />
• Metafont calculations (Metapolation)<br />
• Prototypo calculations<br />
• Font Chamelion calculations :)<br />
• …<br />
• A combination of all :D (that would be another project)<br />
• Or just drawing it, using beziers or a penci!, etc. <br />

No matter what input/output format (open/proprietary): Postscript Type 1, MM, …, OTF, …, UFO3, Glyphs, VFB, Metafont, Prototypo,Knoths Typy, …) 




-------

A more basic visualisation:<br />
![Interpolation Interface](Interpolation-Root-Method_Visualisation.png)

Sliders<br />
![Interpolation Interface](Interpolation-Root-Method_Slider-Interface-Sketch.png)

-----------

And some more sketches for another interface (specific example is inspired by Tim Ahrens RMX Scaler):<br />
![Interpolation Interface](InterpolationInterface_02.png) 


This Example uses a very basic interpolation method (no Root-Method) interpolation, wich makes it really complicated if you have more than two or three masters:<br />
![Interpolation Interface](InterpolationInterface_01.png)<br />
If you leave the parameter thing aside the ›Master-Mode‹ is technically really simple to implement… the hardest thing is to code the interface for it ;) 
(even though simple ›parameters‹ as spacing, kerning, x-Interpolation, y-Interpolation would be quite easy to implement as well) 


# License

The content of this project is licensed under the <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> – So feel free to implement it anywhere!<br /><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Type Design Multiverse</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/Manuel87/Type_Multiverse" property="cc:attributionName" rel="cc:attributionURL">Manuel von Gebhardi</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
