# docgen tool

A simple tool for generaing a MS Word document from the contents of 
RDF files.  An input directory is specified which is traversed and every RDF file encountered is loaded into an rdflib 
ConjunctiveGraph  The triples of this graph a traversed in alphabetical orde by subject, predicate and object and then 
rendered as the contents of the Word file.  There are three options that must be specified

* --directory Source RDF directory
* --output Output MS Word File
* --title Document Title
