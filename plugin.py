symbols = {"pi" : "\pi", "union" : "\cup"}

def appearance():
    import Foundation
    dark_mode = Foundation.NSUserDefaults.standardUserDefaults().persistentDomainForName_(Foundation.NSGlobalDomain).objectForKey_("AppleInterfaceStyle") == "Dark"
    return "dark" if dark_mode else "light"


def generate_html(query, result):
	html = """
		<html>
			<head>
				<style>
					body {
						font-family: 'Helvetica Neue';
						font-size: 16px;
						font-weight: 200;
						text-align: center;
						-webkit-user-select: none;
					}
					.content {
						-webkit-user-select: all;
					}
					h1, h3, h4 {
						font-weight: 200;
					}
                    .tex-img {
                        background-color: #fff;
                        padding: 20px;
                    }
                    .dark {
                        color: #fff;
                        padding: 20px
                    }
                    .light {
                        color: #000;
                        padding: 20px
                    }
				</style>
                <script src="jquery.min.js"></script>
                <script>
                    function process_latex() {
                            $('pre.latex').each(function(e) {
                              var tex = $(this).text();
                              var url = "http://chart.apis.google.com/chart?cht=tx&chs=50&chl=" + encodeURIComponent(tex);
                              var cls = $(this).attr('class');
                              var img = '<img src="' + url + '" alt="' + tex + '" class="' + cls + '"/>';
                              $(img).insertBefore($(this));
                              $(this).hide();
                            });
                          }
                          $(document).ready(function() {process_latex();});
                </script>
			</head>
			<body>
    			
                <div class="tex-img">
                    <pre class="latex">
                        {{symbol}}
                    </pre>
                </div>
    			<div class={{appearance}}>
    				<h1 class="content">{{symbol}}</h1>
    				<br>
    				<h4>Click the command and use &#8984; + C to copy to clipboard.
			    </div>
            </body>
	"""
	html = html.replace("{{appearance}}", appearance())
	html = html.replace("{{query}}", query)
	html = html.replace("{{symbol}}", result)
	return html
    
def results(fields, original_query):
	query = fields['~message']
	result = symbols[query]
	return {
		"title" : "LaTeX Symbol Finder",
		"run_args" : [result],
		"html" : generate_html(query, result),
		"webview_transparent_background" : True
	}

def run(output):
	import os
	os.system('printf "' + output + '" | pbcopy')

