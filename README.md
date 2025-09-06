I couldn't find any other programs or datasets to download legislation in bulk, so I decided to make one myself!  
Also didn't help that there was not much easily accessible information about the existing legislation.gov.uk API, so I had to email the National Archives team that managed it to get sent the link to the documentation (found at the bottom)  

## To-do list
- [ ] Get choices for all parliaments to choose type of legislation
- [ ] Get choices for Welsh primary legislation (senedd vs national assembly)
- [ ] Get SIs working (UK, Scottish)

# Working status of every type of legislation: 
## UK
  UK Public General Acts - COMPLETE (haven't tested anything pre-1988, but it should work in theory, will do more tests)  
  UK Local Acts - WIP  
  UK Private and Personal Acts - WIP  
  UK Statutory Instruments - WIP  
  UK Ministerial Directions - WIP  
  UK Ministerial Orders - WIP  
  UK Statutory Rules and Orders 1900-1948 - WIP  
  UK Draft Statutory Instruments - WIP (Might be difficult due to strange formatting of url)  
  
## Wales
  Acts of Senedd Cymru -  WIP (English language from mid 2020 onwards works)  
  Wales Statutory Instruments - WIP  
  Acts of the National Assembly for Wales - WIP  
  Measures of the National Assembly for Wales - WIP  

## Scotland
  Acts of the Scottish Parliament - COMPLETE (subject to more comprehensive testing) 
  Acts of the Old Scottish Parliament 1424-1707 - WIP  
  Scottish Statutory Instruments - WIP  
  Scottish Draft Statutory Instruments - WIP (Might be difficult due to strange formatting of url)  

## Northern Ireland
  Acts of the Northern Ireland Assembly - COMPLETE (subject to more comprehensive testing)  
  Acts of the Old Irish Parliament 1495-1800 - WIP  
  Northern Ireland Statutory Rules - WIP (Might be incredibly hard to implement due to how the rules are put online)  
  Northern Ireland Orders in Council - WIP  
  Northern Ireland Assembly Measures 1974 - WIP  
  Acts of the Northern Ireland Parliament 1921-1972 - WIP  
  Northern Ireland Statutory Rules and Orders 1922-1973 - WIP  
  Northern Ireland Draft Statutory Rules - WIP  

## API Documentation
https://legislation.github.io/data-documentation/  

http://leggovuk-ldn.s3-website.eu-west-2.amazonaws.com/ (last updated in late 2022, and is now decommisioned)  
