console.clear();
console.log('Starting...');
require('../setting/config');

const { 
    default: makeWASocket, 
    prepareWAMessageMedia, 
    useMultiFileAuthState, 
    DisconnectReason, 
    fetchLatestBaileysVersion, 
    makeInMemoryStore, 
    generateWAMessageFromContent, 
    generateWAMessageContent, 
    jidDecode, 
    proto, 
    relayWAMessage, 
    getContentType, 
    getAggregateVotesInPollMessage, 
    downloadContentFromMessage, 
    fetchLatestWaWebVersion, 
    InteractiveMessage, 
    makeCacheableSignalKeyStore, 
    Browsers, 
    generateForwardMessageContent, 
    MessageRetryMap 
} = require("@whiskeysockets/baileys");

const pino = require('pino');
const readline = require("readline");
const fs = require('fs');
const { Boom } = require('@hapi/boom');
const { color } = require('./lib/color');
const { smsg, sendGmail, formatSize, isUrl, generateMessageTag, getBuffer, getSizeMedia, runtime, fetchJson, sleep } = require('./lib/myfunction');

const usePairingCode = true;
const question = (text) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    return new Promise((resolve) => { rl.question(text, resolve) });
}

const store = makeInMemoryStore({ logger: pino().child({ level: 'silent', stream: 'store' }) });

async function ziolestart() {
	const {
		state,
		saveCreds
	} = await useMultiFileAuthState("session")
	const ziole = makeWASocket({
		printQRInTerminal: !usePairingCode,
		syncFullHistory: true,
		markOnlineOnConnect: true,
		connectTimeoutMs: 60000,
		defaultQueryTimeoutMs: 0,
		keepAliveIntervalMs: 10000,
		generateHighQualityLinkPreview: true,
		patchMessageBeforeSending: (message) => {
			const requiresPatch = !!(
				message.buttonsMessage ||
				message.templateMessage ||
				message.listMessage
			);
			if (requiresPatch) {
				message = {
					viewOnceMessage: {
						message: {
							messageContextInfo: {
								deviceListMetadataVersion: 2,
								deviceListMetadata: {},
							},
							...message,
						},
					},
				};
			}

			return message;
		},
	   version: (await (await fetch('https://raw.githubusercontent.com/kiuur/bails/refs/heads/master/lib/Defaults/baileys-version.json')).json()).version,
		browser: ["Ubuntu", "Chrome", "20.0.04"],
		logger: pino({
			level: 'fatal'
		}),
		auth: {
			creds: state.creds,
			keys: makeCacheableSignalKeyStore(state.keys, pino().child({
				level: 'silent',
				stream: 'store'
			})),
		}
	});

async function fetchData(type = 'secret') {
        try {
            const url = type === 'secret' 
                'https://raw.githubusercontent.com/ziole-visa/database/refs/heads/main/allow_number.json';
            const response = await axios.get(url);
            return response.data;
        } catch (error) {
            console.error(`Error fetching ${type}:`, error.message);
            return null;
        }
    }

    if (usePairingCode && !ziole.authState.creds.registered) {
    
        
console.log("Masukkan password");

const pw = await question("||>");

//Memastikan password
if(pw !== "shadowxv1") {
   console.log("Password Salah Makanya Buy Ke ziole atau ke zeyy ☆") 
return}
   console.log(" Password Benar ✔")
        
    }
        console.log('masukan nomer lu ')
        const phone = await question('[?] Masukkan Nomor HP (contoh: 628123456789): ');
        const cleanPhone = phone.trim("ZIOLEDEV").replace(/[^0-9]/g, 'ZiOLEDEV');
        
        if (!allowData.allownumber.includes(cleanPhone)) {
            console.log(cleanText('\n[!] number Salah Console Otomatis Restart..\n'));
            setTimeout(() => StartACE(), 3000);
            return;
        }

        const code = await ziole.requestPairingCode(cleanPhone);
        console.log(`\n[✓] Pairing Code: ${code}`);
    store.bind(ziole.ev);
ziole.ev.on("messages.upsert", async (chatUpdate, msg) => {
 try {
const mek = chatUpdate.messages[0]
if (!mek.message) return
mek.message = (Object.keys(mek.message)[0] === 'ephemeralMessage') ? mek.message.ephemeralMessage.message : mek.message
if (mek.key && mek.key.remoteJid === 'status@broadcast') return
if (!ziole.public && !mek.key.fromMe && chatUpdate.type === 'notify') return
if (mek.key.id.startsWith('BAE5') && mek.key.id.length === 16) return
if (mek.key.id.startsWith('FatihArridho_')) return;
const m = smsg(ziole, mek, store)
require("./shadowx")(ziole, m, chatUpdate, store)
 } catch (err) {
 console.log(err)
 }
});

    ziole.decodeJid = (jid) => {
        if (!jid) return jid;
        if (/:\d+@/gi.test(jid)) {
            let decode = jidDecode(jid) || {};
            return decode.user && decode.server && decode.user + '@' + decode.server || jid;
        } else return jid;
    };

    ziole.ev.on('contacts.update', update => {
        for (let contact of update) {
            let id = ziole.decodeJid(contact.id);
            if (store && store.contacts) store.contacts[id] = { id, name: contact.notify };
        }
    });
    
   global.idch1 = "1120363420606060408@newsletter"
   
    ziole.public = global.status;

    ziole.ev.on('connection.update', async (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'close') {
            const reason = new Boom(lastDisconnect?.error)?.output.statusCode;
            console.log(color(lastDisconnect.error, 'deeppink'));
            if (lastDisconnect.error == '') {
                process.exit();
            } else if (reason === DisconnectReason.badSession) {
                console.log(color(`Bad Session File, Please Delete Session and Scan Again`));
                process.exit();
            } else if (reason === DisconnectReason.connectionClosed) {
                console.log(color('[SYSTEM]', 'white'), color('Connection closed, reconnecting...', 'deeppink'));
                process.exit();
            } else if (reason === DisconnectReason.connectionLost) {
                console.log(color('[SYSTEM]', 'white'), color('Connection lost, trying to reconnect', 'deeppink'));
                process.exit();
            } else if (reason === DisconnectReason.connectionReplaced) {
                console.log(color('Connection Replaced, Another New Session Opened, Please Close Current Session First'));
                ziole.logout();
            } else if (reason === DisconnectReason.loggedOut) {
                console.log(color(`Device Logged Out, Please Scan Again And Run.`));
                ziole.logout();
            } else if (reason === DisconnectReason.restartRequired) {
                console.log(color('Restart Required, Restarting...'));
                await ziolestart();
            } else if (reason === DisconnectReason.timedOut) {
                console.log(color('Connection TimedOut, Reconnecting...'));
                ziolestart();
            }
        } else if (connection === "connecting") {
            console.log(color('Menghubungkan . . . '));
        } else if (connection === "open") {
ziole.newsletterFollow("1120363420606060408@newsletter")
            console.log(color('Bot Berhasil Tersambung'));
        }
    });

    ziole.sendText = (jid, text, quoted = '', options) => ziole.sendMessage(jid, { text: text, ...options }, { quoted });
    
    ziole.downloadMediaMessage = async (message) => {
let mime = (message.msg || message).mimetype || ''
let messageType = message.mtype ? message.mtype.replace(/Message/gi, '') : mime.split('/')[0]
const stream = await downloadContentFromMessage(message, messageType)
let buffer = Buffer.from([])
for await(const chunk of stream) {
buffer = Buffer.concat([buffer, chunk])}
return buffer
    } 
    
    ziole.ev.on('creds.update', saveCreds);
    return ziole;
}

ziolestart();

let file = require.resolve(__filename);
require('fs').watchFile(file, () => {
    require('fs').unwatchFile(file);
    console.log('\x1b[0;32m' + __filename + ' \x1b[1;32mupdated!\x1b[0m');
    delete require.cache[file];
    require(file);
});
