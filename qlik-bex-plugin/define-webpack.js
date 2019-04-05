var Rx = require('rxjs');
var webpack = require('webpack');
require('babel-polyfill')

module.exports = function(extensionName) {
  return Rx.Observable.create(observer => {
    const compiler = webpack({
      entry: {
        app: ["babel-polyfill", `./src/${extensionName}.js`]
      },
      output: {
        path: `${process.cwd()}/dist/${extensionName}`,
        filename: `${extensionName}.js`
      },
      devtool: 'eval',
      module: {
        loaders: [
          {
            test: /\.js?$/,
            exclude: /node_modules/,
            loader: "babel-loader",
            query: {
              presets: ["env", "stage-0"]
            }
          },
          {
            test: /\.html$/,
            loader: 'html-loader'
          },
          {
            test: /\.scss$/,
            use: [
              { loader: 'style-loader' },
              { loader: 'css-loader' },
              { loader: 'sass-loader' }
            ]
          },
          {
            test: /\.(png|svg|jpg|gif)$/,
            use: [
              {
                loader: 'file-loader',
                options: {
                  name: '[name].[ext]',
                  publicPath: `/extensions/${extensionName}/`
                }
              }
            ]
          }
        ]
      }
    });

    observer.next({ extensionName: extensionName, compiler: compiler })
    observer.complete();
  })
}