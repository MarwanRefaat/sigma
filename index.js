// This file is used to register all your cloud functions in GCP.
// DO NOT EDIT/DELETE THIS, UNLESS YOU KNOW WHAT YOU ARE DOING.

exports.gamefi = require("./gamefi.js").handler;
exports.nodeSandboxFunction = require("./node-sandbox-function.js").handler;