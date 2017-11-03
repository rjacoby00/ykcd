from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>RJ Notification Service</title>

  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.2.1/material.min.js"></script>
  <link rel="stylesheet" href="https://rawgit.com/rjacoby00/rjnotify_pyth/master/styles/index.css">
</head>

<body>

  <header>
    <h1>RJ Notify</h1>
  </header>

  <main>
    <p>Welcome to RJ Notify.  Press the button below to join and get a key.</p>
    <p>
      <button disabled class="js-push-btn mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect">
        Enable RJ Notify
      </button>
    </p>
    <section class="subscription-details js-subscription-details is-invisible">
      <p>Subsribed, here's your key:</p>
      <pre><code class="js-subscription-json"></code></pre>
    </section>
  </main>
  <script src="https://rawgit.com/rjacoby00/rjnotify_pyth/master/scripts/main.js"></script>

  <script src="https://code.getmdl.io/1.2.1/material.min.js"></script>
</body>
</html>
	
'''
@app.route('/sw.js')
def index():
	return'''/*
*
*  Push Notifications codelab
*  Copyright 2015 Google Inc. All rights reserved.
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      https://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License
*
*/

/* eslint-env browser, serviceworker, es6 */

'use srict';
self.addEventListener('push', function(event) {
  console.log('[Service Worker] Push Received.');
  console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);

  const title = 'Push Codelab';
  const options = {
    body: 'Yay it works.',
    icon: 'images/icon.png',
    badge: 'images/badge.png'
  };

  event.waitUntil(self.registration.showNotification(title, options));
});'''
if __name__ == "__main__":
	app.run()
